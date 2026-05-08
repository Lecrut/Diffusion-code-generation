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
        return "Error: Invalid expression format. Only simple addition or subtraction is supported."
if __name__ == '__main__':
    calc = Calculator()
    print("Addition result:")
    result_add = calc.add(10, 5)
    print(f"10 + 5 = {result_add}")
    print("\nSubtraction result:")
    result_sub = calc.subtract(20, 7)
    print(f"20 - 7 = {result_sub}")
    print("\nSolving addition problem:")
    result_solve_add = calc.solve("15 + 8")
    print(f"15 + 8 = {result_solve_add}")
    print("\nSolving subtraction problem:")
    result_solve_sub = calc.solve("30 - 12")
    print(f"30 - 12 = {result_solve_sub}")
    print("\nSolving invalid problem:")
    result_solve_invalid = calc.solve("10 + 5 + 2")
    print(f"10 + 5 + 2 = {result_solve_invalid}")