class SumCalculator:
    def sum_list(self, lst):
        return sum(lst) if lst else 0

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.sum_list([1, 2, 3]))
    print(calculator.sum_list([]))