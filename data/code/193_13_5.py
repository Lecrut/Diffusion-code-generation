class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(SumCalculator.calculate_sum(sample_values))