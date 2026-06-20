OPERATIONS = {
    'addition': lambda x, y: x + y,
    'subtraction': lambda x, y: x - y,
    'multiplication': lambda x, y: x * y,
    'division': lambda x, y: x / y if y != 0 else None
}

class Calculator:
    def execute_operations(self, num1, num2):
        results = {}
        for op, func in OPERATIONS.items():
            results[op] = func(num1, num2)
        return results

if __name__ == '__main__':
    calc = Calculator()
    sample_num1 = 10
    sample_num2 = 5
    operation_results = calc.execute_operations(sample_num1, sample_num2)
    print(operation_results)