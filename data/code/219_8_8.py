class MaxSquaredCalculator:
    def calculate_max_squared(self):
        return max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    calculator = MaxSquaredCalculator()
    print(calculator.calculate_max_squared())