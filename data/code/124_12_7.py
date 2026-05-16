class Calculator:
    def execute_operations(self, numbers):
        results = []
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                operations = {
                    'add': num1 + num2,
                    'subtract': num1 - num2,
                    'multiply': num1 * num2,
                    'divide': None
                }
                if num2 != 0:
                    operations['divide'] = num1 / num2
                results.append({
                    'num1': num1,
                    'num2': num2,
                    'operations': operations
                })
        return results
if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [10, 5, 2]
    output = calc.execute_operations(sample_numbers)
    for item in output:
        print(item)