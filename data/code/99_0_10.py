def evaluate_expression(expression: str) -> float:
    def parse_expression():
        return parse_addition()

    def parse_addition():
        left = parse_multiplication()
        while True:
            skip_spaces()
            if index[0] < len(expression) and expression[index[0]] in ('+', '-'):
                op = expression[index[0]]
                index[0] += 1
                right = parse_multiplication()
                if op == '+':
                    left = left + right
                else:
                    left = left - right
            else:
                break
        return left

    def parse_multiplication():
        left = parse_unary()
        while True:
            skip_spaces()
            if index[0] < len(expression) and expression[index[0]] in ('*', '/'):
                op = expression[index[0]]
                index[0] += 1
                right = parse_unary()
                if op == '*':
                    left = left * right
                else:
                    if right == 0:
                        raise ZeroDivisionError("division by zero")
                    left = left / right
            else:
                break
        return left

    def parse_unary():
        skip_spaces()
        if index[0] < len(expression) and expression[index[0]] == '-':
            index[0] += 1
            operand = parse_unary()
            return -operand
        if index[0] < len(expression) and expression[index[0]] == '+':
            index[0] += 1
            return parse_unary()
        return parse_primary()

    def parse_primary():
        skip_spaces()
        if index[0] < len(expression) and expression[index[0]] == '(':
            index[0] += 1
            result = parse_expression()
            skip_spaces()
            if index[0] < len(expression) and expression[index[0]] == ')':
                index[0] += 1
            else:
                raise ValueError("Mismatched parentheses")
            return result
        return parse_number()

    def parse_number():
        skip_spaces()
        start = index[0]
        if index[0] < len(expression) and expression[index[0]] == '-':
            index[0] += 1
        while index[0] < len(expression) and (expression[index[0]].isdigit() or expression[index[0]] == '.'):
            index[0] += 1
        if index[0] == start or (start < len(expression) and expression[start] == '-'):
            if start < len(expression) and expression[start] == '-':
                if index[0] == start + 1:
                    raise ValueError("Invalid number")
            else:
                raise ValueError("Invalid number")
        num_str = expression[start:index[0]]
        if '.' in num_str:
            return float(num_str)
        return int(num_str)

    def skip_spaces():
        while index[0] < len(expression) and expression[index[0]] == ' ':
            index[0] += 1

    index = [0]
    result = parse_expression()
    skip_spaces()
    if index[0] != len(expression):
        raise ValueError("Unexpected characters at end of expression")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("(1 + 2) * (3 + 4)"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("2 ** 3"))
    print(evaluate_expression("100 / (5 - 3)"))