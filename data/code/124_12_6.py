class Calculator:
    def execute_operations(self, numbers):
        results = []
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                results.append((num1, num2, '+', num1 + num2))
                results.append((num1, num2, '-', num1 - num2))
                results.append((num1, num2, '*', num1 * num2))
                if num2 != 0:
                    results.append((num1, num2, '/', num1 / num2))
        return results
if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [2, 3, 4]
    operation_results = calc.execute_operations(sample_numbers)
    for res in operation_results:
        print(f"({res[0]} {res[2]} {res[1]}) = {res[3]}")