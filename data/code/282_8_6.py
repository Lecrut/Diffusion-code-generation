class SumCalculator:
    def __init__(self):
        self.total = 0

    @staticmethod
    def add_numbers(numbers):
        total = 0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    sample_numbers = [10, -5, 3, -2, 4]
    calculator = SumCalculator()
    result = calculator.add_numbers(sample_numbers)
    print(result)