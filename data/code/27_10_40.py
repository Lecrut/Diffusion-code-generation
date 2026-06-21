class PrecisionChecker:
    def __init__(self, precision=1e-10):
        self.precision = precision

    def check_difference(self, value1, value2):
        return abs(value1 - value2) > self.precision

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    precision_checker = PrecisionChecker()
    result = precision_checker.check_difference(value1, value2)
    print(result)