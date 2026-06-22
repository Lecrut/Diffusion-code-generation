class MaxSquaredCalculator:
    MAX_NUMBER = 100

    @staticmethod
    def calculate_max_squared():
        return max(x**2 for x in range(1, MaxSquaredCalculator.MAX_NUMBER + 1))

if __name__ == '__main__':
    calculator = MaxSquaredCalculator()
    max_value = calculator.calculate_max_squared()
    print(max_value)