class RatioManipulator:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = num
        self.den = den
    def multiply_ratio(self, factor):
        if not isinstance(factor, int):
            raise TypeError("Factor must be an integer")
        self.num *= factor
        self.den *= factor
if __name__ == '__main__':
    initial_num = 10
    initial_den = 5
    ratio_manipulator = RatioManipulator(initial_num, initial_den)
    print(f"Initial ratio: {ratio_manipulator.num}/{ratio_manipulator.den}")
    factor = 3
    ratio_manipulator.multiply_ratio(factor)
    print(f"Ratio after multiplying by {factor}: {ratio_manipulator.num}/{ratio_manipulator.den}")
    factor = -2
    ratio_manipulator.multiply_ratio(factor)
    print(f"Ratio after multiplying by {factor}: {ratio_manipulator.num}/{ratio_manipulator.den}")
    try:
        RatioManipulator(10, 0)
    except ValueError as e:
        print(f"Error caught for zero denominator: {e}")