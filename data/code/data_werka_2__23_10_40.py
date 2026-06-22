class FloatEqualityChecker:
    DEFAULT_TOLERANCE = 1e-9

    def __init__(self, tolerance=None):
        self.set_tolerance(tolerance)

    def set_tolerance(self, new_tolerance):
        if new_tolerance is not None and new_tolerance < 0:
            raise ValueError("Tolerance must be non-negative")
        self.tolerance = new_tolerance if new_tolerance is not None else self.DEFAULT_TOLERANCE

    def are_equal(self, num1, num2):
        return abs(num1 - num2) <= self.tolerance

def validate_float(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Both values must be numbers")

if __name__ == '__main__':
    value1 = 0.1 + 0.2
    value2 = 0.3

    validate_float(value1)
    validate_float(value2)

    checker = FloatEqualityChecker()
    result = checker.are_equal(value1, value2)
    print(result)