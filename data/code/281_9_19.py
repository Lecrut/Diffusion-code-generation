class NumberSumCalculator:
    def __init__(self):
        self.numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = NumberSumCalculator()
    total_sum = calculator.calculate_sum()
    print(f"Total Sum of Twelve Numbers: {total_sum}")