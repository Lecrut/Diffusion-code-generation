class Calculator:
    def __init__(self):
        self.operation_map = {
            'add': self.add,
        }

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        return a + b

    def perform_operation(self, operation_name, *args):
        operation = self.operation_map.get(operation_name)
        if operation:
            return operation(*args)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.perform_operation('add', 8, 2)
        print(f"Result of add(8, 2): {result1}")
        
        result2 = calc.perform_operation('add', 12.5, 7.5)
        print(f"Result of add(12.5, 7.5): {result2}")
    except ValueError as e:
        print(e)