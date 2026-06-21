class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_list = [1, 5, 10, -3, 8]
    result = calculator.calculate_sum(sample_list)
    print(result)