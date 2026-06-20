import operator

class Calculator:
    OPERATIONS = {
        'add': operator.add,
        'sub': operator.sub,
        'mul': operator.mul,
        'div': operator.truediv
    }

    @staticmethod
    def perform_operations(a, b):
        results = {}
        for op_name, op_func in Calculator.OPERATIONS.items():
            try:
                result = op_func(a, b)
            except ZeroDivisionError:
                result = "Cannot divide by zero"
            results[op_name] = result
        return results

if __name__ == '__main__':
    sample_values = (15, 3)
    calc = Calculator()
    print(calc.perform_operations(*sample_values))