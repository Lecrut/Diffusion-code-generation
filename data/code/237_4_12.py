class TriangularNumberGenerator:
    def __init__(self):
        self.triangular_numbers = [n * (n + 1) // 2 for n in range(1, 13)]

    def get_first_n_triangular_numbers(self, n):
        return self.triangular_numbers[:n]

if __name__ == '__main__':
    generator = TriangularNumberGenerator()
    first_6 = generator.get_first_n_triangular_numbers(6)
    first_12 = generator.get_first_n_triangular_numbers(12)
    print(first_6)
    print(first_12)