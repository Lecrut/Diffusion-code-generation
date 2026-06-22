class MaxSquaredCalculator:
    MAX_VALUE = 100

    @staticmethod
    def calculate_max_squared():
        return max(x**2 for x in range(1, MaxSquaredCalculator.MAX_VALUE + 1))

if __name__ == '__main__':
    max_value = MaxSquaredCalculator.calculate_max_squared()
    print(max_value)