class FloatSumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_list = [1.5, 2.75, 3.0, -4.2, 0.1]
    result = FloatSumCalculator.calculate_sum(sample_list)
    print(result)