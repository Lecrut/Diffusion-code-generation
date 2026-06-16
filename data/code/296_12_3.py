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
    manipulator = RatioManipulator(initial_num, initial_den)
    print(f"Initial ratio: {manipulator.num}/{manipulator.den}")
    factor1 = 3
    manipulator.multiply_ratio(factor1)
    print(f"Ratio after multiplying by {factor1}: {manipulator.num}/{manipulator.den}")
    factor2 = -2
    manipulator.multiply_ratio(factor2)
    print(f"Ratio after multiplying by {factor2}: {manipulator.num}/{manipulator.den}")
    try:
        invalid_manipulator = RatioManipulator(10, 0)
        invalid_manipulator.multiply_ratio(2)
    except ValueError as e:
        print(f"Error caught for zero denominator: {e}")
    except TypeError as e:
        print(f"Error caught for invalid factor type: {e}")