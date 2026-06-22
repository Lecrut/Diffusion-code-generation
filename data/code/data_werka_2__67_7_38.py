class Calculator:
    def __init__(self):
        self.supported_operations = ['add']

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        return a + b

    def perform_operation(self, operation_name, *args):
        if operation_name == 'add':
            if len(args) != 2:
                raise ValueError("Add operation requires exactly two arguments.")
            return self.add(*args)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")

if __name__ == '__main__':
    calc = Calculator()
    try:
        result = calc.perform_operation('add', 8, 12)
        print(result)
        invalid_result = calc.perform_operation('add', 'a', 3)
    except ValueError as e:
        print(e)