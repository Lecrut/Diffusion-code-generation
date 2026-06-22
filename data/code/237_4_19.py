class TriangularNumbersCalculator:
    def calculate_triangular_numbers(self, count):
        return [n * (n + 1) // 2 for n in range(1, count + 1)]

if __name__ == '__main__':
    calculator = TriangularNumbersCalculator()
    sample_count = 12
    triangular_result = calculator.calculate_triangular_numbers(sample_count)
    print(triangular_result)