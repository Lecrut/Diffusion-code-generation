class SumCalculator:
    def calculate_sum(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    calculator = SumCalculator()
    result = calculator.calculate_sum(sample_list)
    print(result)