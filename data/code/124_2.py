class ArithmeticCalculator:
    def execute_operations(self, num1, num2):
        results = {}
        results['addition'] = num1 + num2
        results['subtraction'] = num1 - num2
        results['multiplication'] = num1 * num2
        if num2 != 0:
            results['division'] = num1 / num2
        else:
            results['division'] = "Division by zero error"
        return results
if __name__ == '__main__':
    calc = ArithmeticCalculator()
    a = 20
    b = 5
    results = calc.execute_operations(a, b)
    print(results)