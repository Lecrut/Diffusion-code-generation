class TriangularNumbersCalculator:
    def __init__(self):
        self.triangular_numbers = [n * (n + 1) // 2 for n in range(1, 13)]

    def get_first_12(self):
        return self.triangular_numbers

if __name__ == '__main__':
    calculator = TriangularNumbersCalculator()
    print(calculator.get_first_12())