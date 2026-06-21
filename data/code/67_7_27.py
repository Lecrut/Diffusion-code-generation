class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 2)
        print(f"Result of add(8, 2): {result1}")
        
        result2 = calc.add(-5.5, 3.2)
        print(f"Result of add(-5.5, 3.2): {result2}")
    except ValueError as e:
        print(e)