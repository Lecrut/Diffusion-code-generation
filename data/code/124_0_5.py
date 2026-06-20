import operator

class Calculator:
    OPERATIONS = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': operator.truediv
    }

    @staticmethod
    def perform_operation(op_name, a, b):
        try:
            return Calculator.OPERATIONS[op_name](a, b)
        except ZeroDivisionError:
            return "Cannot divide by zero"

if __name__ == '__main__':
    calc = Calculator()
    sample_values = (15, 3)
    operations = ['add', 'sub', 'mul', 'div']
    
    for op in operations:
        result = calc.perform_operation(op, *sample_values)
        print(f"{op.upper()}: {result}")