class ArithmeticCalculator:
    ZERO_COUNT_HANDLING = 0

    @staticmethod
    def _get_sample_data():
        return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    def calculate_average(self, numbers):
        if not numbers:
            return self.ZERO_COUNT_HANDLING
        total = sum(numbers)
        count = len(numbers)
        return total / count

if __name__ == '__main__':
    calculator = ArithmeticCalculator()
    sample_data = calculator._get_sample_data()
    result = calculator.calculate_average(sample_data)
    print(result)