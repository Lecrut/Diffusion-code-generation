class ArithmeticCalculator:
    def execute_operations(self, num1, num2):
        results = {
            "addition": num1 + num2,
            "subtraction": num1 - num2,
            "multiplication": num1 * num2,
            "division": num1 / num2
        }
        return results
if __name__ == '__main__':
    calculator = ArithmeticCalculator()
    a = 20
    b = 5
    results = calculator.execute_operations(a, b)
    print(results)