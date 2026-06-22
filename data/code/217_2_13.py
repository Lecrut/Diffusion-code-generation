class FloatingPointComparer:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def compare(self, a, b):
        if abs(a - b) <= self.tolerance:
            return "equal"
        elif a > b:
            return "larger"
        else:
            return "smaller"

if __name__ == '__main__':
    comparer = FloatingPointComparer()
    num1 = 0.1 + 0.2
    num2 = 0.3
    result1 = comparer.compare(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 1.0
    num4 = 1.00000000001
    result2 = comparer.compare(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")