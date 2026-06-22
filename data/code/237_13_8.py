class TriangularNumbers:
    @staticmethod
    def generate_terms(n):
        return [int(n * (n + 1) / 2) for n in range(1, n + 1)]

if __name__ == '__main__':
    sample_values = TriangularNumbers.generate_terms(12)
    print(sample_values)