class ListSumCalculator:
    def calculate_sum(self, iterable: list) -> int:
        return sum(iterable)

if __name__ == '__main__':
    calculator = ListSumCalculator()
    print(calculator.calculate_sum([1, 2, 3, 4, 5]))
    print(calculator.calculate_sum([10, -5, 20, 0]))
    print(calculator.calculate_sum([]))
    print(calculator.calculate_sum([100]))