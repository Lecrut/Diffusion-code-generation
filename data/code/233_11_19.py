class SymbolMatrixGenerator:
    def __init__(self, width, height, symbol):
        self.width = width
        self.height = height
        self.symbol = symbol

    def generate_matrix(self):
        return '\n'.join([self.symbol * self.width for _ in range(self.height)])

if __name__ == '__main__':
    generator = SymbolMatrixGenerator(5, 4, '*')
    matrix = generator.generate_matrix()
    print(matrix)