class FloatingPointComparer:
    TOLERANCE = 1e-9

    @staticmethod
    def compare(a, b):
        if abs(a - b) <= FloatingPointComparer.TOLERANCE:
            return "equal"
        elif a > b:
            return "larger"
        else:
            return "smaller"

if __name__ == '__main__':
    comparer = FloatingPointComparer()
    result1 = comparer.compare(0.1 + 0.2, 0.3)
    print(f"Comparing 0.1 + 0.2 and 0.3: {result1}")
    result2 = comparer.compare(1.0, 1.00000000001)
    print(f"Comparing 1.0 and 1.00000000001: {result2}")