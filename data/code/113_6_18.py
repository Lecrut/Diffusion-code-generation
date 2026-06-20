class ArithmeticOperations:
    MIN_VALUE = 0

    @staticmethod
    def subtract(a, b):
        result = a - b
        if result < ArithmeticOperations.MIN_VALUE:
            raise ValueError("Subtraction resulted in a negative number")
        return result

if __name__ == '__main__':
    a1 = 100
    b1 = 45
    try:
        result1 = ArithmeticOperations.subtract(a1, b1)
        print(f"Result of {a1} - {b1}: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    a2 = 50
    b2 = 150
    try:
        result2 = ArithmeticOperations.subtract(a2, b2)
        print(f"Result of {a2} - {b2}: {result2}")
    except ValueError as e:
        print(f"Error: {e}")