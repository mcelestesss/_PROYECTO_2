class Mapa:
    """
    Clase que representa el mapa del laberinto.
    Define la estructura y forma del laberinto.
    """
    
    def __init__(self, ancho, alto):
        """
        Inicializa el mapa del laberinto.
        
        Args:
            ancho (int): Ancho del laberinto
            alto (int): Alto del laberinto
        """
        self.ancho = ancho
        self.alto = alto
        self.laberinto = [[0 for _ in range(ancho)] for _ in range(alto)]
    
    def crear_laberinto(self):
        """
        Crea la forma inicial del laberinto.
        """
        # Inicializa las paredes (1) y caminos (0)
        for i in range(self.alto):
            for j in range(self.ancho):
                if i == 0 or i == self.alto - 1 or j == 0 or j == self.ancho - 1:
                    self.laberinto[i][j] = 1  # Paredes
                else:
                    self.laberinto[i][j] = 0  # Caminos
    
    def mostrar(self):
        """
        Muestra el laberinto en consola.
        """
        for fila in self.laberinto:
            print(' '.join('█' if celda == 1 else ' ' for celda in fila))
    
    def obtener_laberinto(self):
        """
        Retorna la matriz del laberinto.
        
        Returns:
            list: Matriz que representa el laberinto
        """
        return self.laberinto
