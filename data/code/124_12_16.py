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
                        "addition": self.add(num1, num2),
                        "subtraction": self.subtract(num1, num2),
                        "multiplication": self.multiply(num1, num2),
                        "division": self.divide(num1, num2)
                    })
                else:
                    results.append({
                        "num1": num1,
                        "num2": num2,
                        "addition": None,
                        "subtraction": None,
                        "multiplication": None,
                        "division": None
                    })
        return results

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return None

if __name__ == '__main__':
    calc = Calculator()
    sample_numbers = [10, 5, 2]
    operation_results = calc.execute_operations(sample_numbers)
    for result in operation_results:
        print(result)