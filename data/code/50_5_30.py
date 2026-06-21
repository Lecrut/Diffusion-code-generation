class NonNegativeDifference:
    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        self.a = a
        self.b = b

    def get_difference(self):
        return max(0, abs(self.a - self.b))

if __name__ == '__main__':
    diff_calculator = NonNegativeDifference(-15, 25)
    print(diff_calculator.get_difference())