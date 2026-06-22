class TriangularNumbers:
    MAX_COUNT = 12

    @staticmethod
    def generate():
        return [n * (n + 1) // 2 for n in range(1, TriangularNumbers.MAX_COUNT + 1)]

if __name__ == '__main__':
    triangular_result = TriangularNumbers.generate()
    print(triangular_result)