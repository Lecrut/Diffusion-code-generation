class ListSumCalculator:
    def __init__(self, data_list):
        self.data_list = data_list

    def calculate_sum(self):
        return sum(self.data_list)

if __name__ == '__main__':
    calculator = ListSumCalculator([1.5, 2.5, 3.5])
    result = calculator.calculate_sum()
    print(result)