class Calculator:
    def execute_operations(self, numbers):
        results = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else None
        }
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2:
                    for op, func in operations.items():
                        result = func(num1, num2)
                        results.append({
                            "num1": num1,
                            "num2": num2,
                            "operation": op,
                            "result": result
                        })
        return results

if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [10, 5, 2]
    operation_results = calc.execute_operations(sample_numbers)
    for result in operation_results:
        print(result)