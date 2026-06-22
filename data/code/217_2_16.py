class FloatToleranceComparer:
    def __init__(self, tolerance=1e-9):
        self.tolerance = tolerance

    def are_close(self, a, b):
        return abs(a - b) <= self.tolerance

if __name__ == '__main__':
    comparer = FloatToleranceComparer()
    num1 = 0.1 + 0.2
    num2 = 0.3
    result1 = comparer.are_close(num1, num2)
    print(f"Are {num1} and {num2} close? {result1}")
    
    num3 = 1.0
    num4 = 1.00000000001
    result2 = comparer.are_close(num3, num4)
    print(f"Are {num3} and {num4} close? {result2}")