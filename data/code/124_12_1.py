class Calculator:
    def execute_operations(self, numbers):
        results = []
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                num1 = numbers[i]
                num2 = numbers[j]
                if num2 != 0:
                    results.append({
                        "num1": num1,
                        "num2": num2,
                        "addition": num1 + num2,
                        "subtraction": num1 - num2,
                        "multiplication": num1 * num2,
                        "division": num1 / num2
                    })
                else:
                    results.append({
                        "num1": num1,
                        "num2": num2,
                        "addition": "Undefined (Division by Zero)",
                        "subtraction": "Undefined (Division by Zero)",
                        "multiplication": "Undefined (Division by Zero)",
                        "division": "Undefined (Division by Zero)"
                    })
        return results
if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [10, 5, 2, 0]
    operation_results = calc.execute_operations(sample_numbers)
    for result in operation_results:
        print(result)