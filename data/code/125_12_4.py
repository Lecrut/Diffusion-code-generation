class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def solve(self, expression):
        if ' + ' in expression:
            parts = expression.split(' + ')
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    return self.add(num1, num2)
                except ValueError:
                    return "Error: Invalid numbers in addition expression"
        elif ' - ' in expression:
            parts = expression.split(' - ')
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    return self.subtract(num1, num2)
                except ValueError:
                    return "Error: Invalid numbers in subtraction expression"
        return "Error: Unsupported operation or invalid expression format"
if __name__ == '__main__':
    calc = Calculator()
    result_add = calc.add(10, 5)
    print(f"10 + 5 = {result_add}")
    result_sub = calc.subtract(10, 5)
    print(f"10 - 5 = {result_sub}")
    result_solve_add = calc.solve("15 + 7")
    print(f"Solving '15 + 7': {result_solve_add}")
    result_solve_sub = calc.solve("20 - 8")
    print(f"Solving '20 - 8': {result_solve_sub}")
    result_solve_invalid = calc.solve("10 + hello")
    print(f"Solving '10 + hello': {result_solve_invalid}")
    result_solve_unknown = calc.solve("10 * 2")
    print(f"Solving '10 * 2': {result_solve_unknown}")