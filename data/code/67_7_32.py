class Calculator:
    def __init__(self):
        self.validators = {
            'add': lambda a, b: isinstance(a, (int, float)) and isinstance(b, (int, float))
        }

    def add(self, a, b):
        if not self.validators['add'](a, b):
            raise ValueError("Both operands must be numbers.")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 4)
        print(f"Result of add(8, 4): {result1}")
        result2 = calc.add(12.5, 7.5)
        print(f"Result of add(12.5, 7.5): {result2}")
    except ValueError as e:
        print(e)