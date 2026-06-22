class Calculator:

    def __init__(self):
        self.operations = {'add': self.add}

    def add(self, a, b):
        return a + b

    def perform_operation(self, operation_name, *args):
        if operation_name in self.operations:
            return self.operations[operation_name](*args)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")
if __name__ == '__main__':
    calc = Calculator()
    result = calc.perform_operation('add', 10, 7)
    print(result)