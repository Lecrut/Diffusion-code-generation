import operator

class Calculator:
    def __init__(self):
        self.operations = {
            'add': operator.add,
            'sub': operator.sub,
            'mul': operator.mul,
            'div': operator.truediv
        }

    def perform_operation(self, op_name, a, b):
        try:
            result = self.operations[op_name](a, b)
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        return result

if __name__ == '__main__':
    calc = Calculator()
    sample_values = (15, 3)
    print("Addition:", calc.perform_operation('add', *sample_values))
    print("Subtraction:", calc.perform_operation('sub', *sample_values))
    print("Multiplication:", calc.perform_operation('mul', *sample_values))
    print("Division:", calc.perform_operation('div', *sample_values))