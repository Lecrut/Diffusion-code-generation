def sum_even_numbers(start, end):
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

class RangeSum:
    def __init__(self, start=0, end=10):
        self.start = start
        self.end = end
    
    def calculate_sum(self):
        return sum_even_numbers(self.start, self.end)

if __name__ == '__main__':
    calculator = RangeSum(1, 10)
    print(calculator.calculate_sum())
    calculator = RangeSum(5, 15)
    print(calculator.calculate_sum())