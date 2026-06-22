class MiddleValueCalculator:
    def __init__(self, data):
        self.data = sorted(data)

    def get_middle_value(self):
        n = len(self.data)
        if n == 0:
            return None
        mid_index = (n - 1) // 2
        return self.data[mid_index]

if __name__ == '__main__':
    calculator = MiddleValueCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print("Middle value:", calculator.get_middle_value())
    calculator_large = MiddleValueCalculator(list(range(1000000)))
    print("Middle value for large list:", calculator_large.get_middle_value())
    calculator_odd = MiddleValueCalculator([2, 7, 1, 8, 2])
    print("Middle value for odd length list:", calculator_odd.get_middle_value())