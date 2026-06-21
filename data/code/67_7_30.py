class Calculator:
    def __init__(self):
        self.total_operations = 0

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        result = a + b
        self.total_operations += 1
        return result

    def get_total_operations(self):
        return self.total_operations

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 4)
        print(f"Result of add(8, 4): {result1}")
        result2 = calc.add(20.75, 12.25)
        print(f"Result of add(20.75, 12.25): {result2}")
        print(f"Total operations performed: {calc.get_total_operations()}")
    except ValueError as e:
        print(e)