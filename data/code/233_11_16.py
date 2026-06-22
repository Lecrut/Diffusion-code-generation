class SymbolMatrixGenerator:
    DEFAULT_SYMBOL = '*'
    
    @staticmethod
    def generate_matrix(rows, cols, symbol=DEFAULT_SYMBOL):
        return '\n'.join([symbol * cols for _ in range(rows)])
    
if __name__ == '__main__':
    generator = SymbolMatrixGenerator()
    matrix = generator.generate_matrix(5, 10)
    print(matrix)