class Calculator:
    def execute_operations(self, numbers):
        results = []
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                operations = [
                    (num1 + num2),
                    (num1 - num2),
                    (num1 * num2),
                    (num2 - num1),
                    (num2 * num1),
                    (num1 / num2) if num2 != 0 else None,
                    (num2 / num1) if num1 != 0 else None
                ]
                for res in operations:
                    if res is not None:
                        results.append((num1, num2, 'add', res))
                        results.append((num1, num2, 'subtract', num1 - num2))
                        results.append((num1, num2, 'multiply', num1 * num2))
                        results.append((num1, num2, 'divide', num1 / num2))
                        results.append((num1, num2, 'subtract_rev', num2 - num1))
                        results.append((num1, num2, 'divide_rev', num2 / num1))
        return results
if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [10, 5, 2]
    operation_results = calc.execute_operations(sample_numbers)
    for result in operation_results:
        print(result)