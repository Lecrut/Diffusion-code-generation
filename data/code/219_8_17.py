class MaxSquaredCalculator:
    MAX_VALUE = 100

    @staticmethod
    def calculate_max_squared():
        return max(x**2 for x in range(1, MaxSquaredCalculator.MAX_VALUE + 1))

if __name__ == '__main__':
    calculator = MaxSquaredCalculator()
    print(calculator.calculate_max_squared())