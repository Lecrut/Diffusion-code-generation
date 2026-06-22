class TriangularNumbers:
    @staticmethod
    def generate(n):
        return [n * (n + 1) // 2 for n in range(1, n + 1)]

if __name__ == '__main__':
    sample_values = 12
    result = TriangularNumbers.generate(sample_values)
    print(result)