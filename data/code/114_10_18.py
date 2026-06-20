class MathOperations:
    @staticmethod
    def multiply_numbers(a, b):
        return a * b

if __name__ == '__main__':
    calculator = MathOperations()
    result1 = calculator.multiply_numbers(5, 4)
    print(f"5 * 4 = {result1}")
    result2 = calculator.multiply_numbers(-3, 7)
    print(f"-3 * 7 = {result2}")