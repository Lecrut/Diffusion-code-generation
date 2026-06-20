operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b if b != 0 else 'Error: Division by zero'}

def evaluate(expression):
    parts = expression.split()
    if len(parts) != 3:
        return 'Error: Invalid expression'
    num1, operator, num2 = parts
    try:
        num1, num2 = (float(num1), float(num2))
        return operators[operator](num1, num2)
    except KeyError:
        return 'Error: Unsupported operator'
if __name__ == '__main__':
    print(evaluate('3 + 5'))
    print(evaluate('10 - 2'))
    print(evaluate('4 * 7'))
    print(evaluate('8 / 2'))
    print(evaluate('5 / 0'))
    print(evaluate('6 % 3'))
    print(evaluate('1 +'))