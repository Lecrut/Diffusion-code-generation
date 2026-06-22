class SumCalculator:
    @staticmethod
    def calculate_total(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, -5, 3, -2, 4]
    calculator = SumCalculator()
    result = calculator.calculate_total(sample_numbers)
    print(result)