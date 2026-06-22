class Calculator:
    def calculate_operations(self, a: int, b: int) -> dict:
        return {
            'addition': a + b,
            'subtraction': a - b,
            'multiplication': a * b,
            'division': a / b if b != 0 else None
        }

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.calculate_operations(10, 5)
    print(f"Operations for 10 and 5: {result1}")
    result2 = calc.calculate_operations(7, 7)
    print(f"Operations for 7 and 7: {result2}")