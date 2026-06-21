class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    my_list = [1, 5, 10.5, 2]
    calculator = SumCalculator()
    print(calculator.calculate_sum(my_list))