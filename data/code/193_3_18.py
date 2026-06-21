class SumCalculator:
    def sum_elements(self, lst):
        return sum(lst) if lst else 0

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.sum_elements([10, 20, 30, 40]))
    print(calculator.sum_elements([]))