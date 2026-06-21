class NumberSum:
    def sum_numbers(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = NumberSum()
    sample1 = [10, 20, 30]
    sample2 = []
    print(calculator.sum_numbers(sample1))
    print(calculator.sum_numbers(sample2))