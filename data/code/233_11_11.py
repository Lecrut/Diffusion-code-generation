class SymbolMatrix:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol
        self.matrix = self._generate_matrix()

    def _generate_matrix(self):
        return '\n'.join([self.symbol * self.width for _ in range(self.height)])

if __name__ == '__main__':
    matrix_instance = SymbolMatrix(5, 3, '*')
    print(matrix_instance._generate_matrix())