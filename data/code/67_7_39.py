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
        result1 = calc.add(5, 3)
        print(f"Result of add(5, 3): {result1}")
        result2 = calc.add(10.5, 7.2)
        print(f"Result of add(10.5, 7.2): {result2}")
        operations_count = calc.get_total_operations()
        print(f"Total operations performed: {operations_count}")
    except ValueError as e:
        print(e)