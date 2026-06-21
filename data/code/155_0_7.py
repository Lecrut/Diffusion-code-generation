class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = SumCalculator.calculate_sum(sample_list)
    print(result)