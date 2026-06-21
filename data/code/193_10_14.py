class SumCalculator:
    def calculate_sum(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_list = [1, 5, 10, -3, 8]
    print(calculator.calculate_sum(sample_list))
    empty_list = []
    print(calculator.calculate_sum(empty_list))