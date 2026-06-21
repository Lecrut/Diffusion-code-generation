class SumCalculator:
    def calculate_sum(self, lst):
        return sum(lst) if lst else 0

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.calculate_sum([10, 20, 30, 40]))
    print(calculator.calculate_sum([]))