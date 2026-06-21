class ValueDifferencer:
    def __init__(self, tolerance=1e-10):
        self.tolerance = tolerance

    def are_values_different(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be either int or float.")
        return abs(value1 - value2) > self.tolerance

if __name__ == '__main__':
    differencer = ValueDifferencer()
    value1 = 10
    value2 = 10.00000000000001
    result = differencer.are_values_different(value1, value2)
    print(result)