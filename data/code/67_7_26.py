class Calculator:
    def __init__(self):
        self.valid_operations = ['add']

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        return a + b

    def perform_operation(self, operation_name, *args):
        if operation_name == 'add':
            if len(args) != 2:
                raise ValueError("Addition requires exactly two arguments.")
            return self.add(*args)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.perform_operation('add', 8, 6)
        print(f"Result of add(8, 6): {result1}")
        result2 = calc.perform_operation('add', 12.5, 4.75)
        print(f"Result of add(12.5, 4.75): {result2}")
    except ValueError as e:
        print(e)