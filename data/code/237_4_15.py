class TriangularNumberGenerator:
    def __init__(self):
        self.triangular_numbers = [n * (n + 1) // 2 for n in range(1, 13)]

    def get_triangular_numbers(self):
        return self.triangular_numbers

if __name__ == '__main__':
    generator = TriangularNumberGenerator()
    print(generator.get_triangular_numbers())