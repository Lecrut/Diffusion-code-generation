class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40]
    result = SumCalculator.calculate_sum(sample_numbers)
    print(result)