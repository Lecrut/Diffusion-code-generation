class FloatToleranceComparer:
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
    comparer = FloatToleranceComparer()
    num1 = 3.141592653589793
    num2 = 3.141592653589794
    result1 = comparer.compare(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    
    num3 = 0.0000001
    num4 = 0.0000002
    result2 = comparer.compare(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")