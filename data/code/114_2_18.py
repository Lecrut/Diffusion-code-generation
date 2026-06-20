class DecimalMultiplier:
    def __init__(self, precision=10):
        self.precision = precision

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        
        result = a * b
        return round(result, self.precision)

if __name__ == '__main__':
    dm = DecimalMultiplier(precision=5)
    result1 = dm.multiply(0.1, 0.2)
    result2 = dm.multiply(3.5, 4.2)
    print("Result of 0.1 * 0.2:", result1)
    print("Result of 3.5 * 4.2:", result2)