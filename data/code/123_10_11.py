class SumCalculator:
    @staticmethod
    def calculate_total_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 5, 42, 18]
    total_sum = SumCalculator.calculate_total_sum(sample_numbers)
    print(total_sum)