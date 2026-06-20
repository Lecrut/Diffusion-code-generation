class SafeDivider:
    DEFAULT_RESULT = float('nan')

    @staticmethod
    def divide(dividend: float, divisor: float) -> float:
        if divisor == 0:
            return SafeDivider.DEFAULT_RESULT
        else:
            return dividend / divisor
if __name__ == '__main__':
    result1 = SafeDivider.divide(10.0, 2.0)
    print(result1)
    result2 = SafeDivider.divide(5.0, 0.0)
    print(result2)