class AbsoluteDifference:
    def calculate(self, a, b):
        return (a - b) & ((a - b) >> 31)

if __name__ == '__main__':
    diff_calculator = AbsoluteDifference()
    print(diff_calculator.calculate(1234567890123456789, 9876543210987654321))
    print(diff_calculator.calculate(-100, -200))
    print(diff_calculator.calculate(0, 0))
    print(diff_calculator.calculate(2**64 - 1, 1))