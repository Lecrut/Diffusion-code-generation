import re
def evaluate_expression(expression):
    tokens = re.findall(r'(\d+\.?\d*|\+|\-|\*|\/|\(|\))', expression)
    values = []
    operators = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or (token.replace('.', '', 1).isdigit()):
            values.append(float(token))
        elif token in ('+', '-', '*', '/', '(', ')'):
            operators.append(token)
        i += 1
    output_values = []
    while i < len(operators):
        op = operators[i]
        if op in ('+', '-', '*', '/'):
            operand1 = values[len(output_values) - 1]
            operand2 = values[len(output_values) - 2]
            if len(output_values) < 2:
                break
            operand2 = values[len(output_values) - 1]
            operand1 = values[len(output_values) - 2]
            if op == '+':
                result = operand1 + operand2
            elif op == '-':
                result = operand1 - operand2
            elif op == '*':
                result = operand1 * operand2
            elif op == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero")
                result = operand1 / operand2
            values.pop()
            values.append(result)
            output_values.append(op)
        else:
            i += 1
    while i < len(operators):
        op = operators[i]
        if op == '(':
            output_values.append(values.pop())
            i += 1
        elif op == ')':
            if len(output_values) < 2:
                raise ValueError("Mismatched parentheses")
            while output_values[-1] != '(':
                op = output_values.pop()
                values.append(op)
            output_values.pop()
            i += 1
        else:
            i += 1
    if not values:
        return 0.0
    return values[0]
if __name__ == '__main__':
    expression1 = "3 + 4 * 2"
    result1 = evaluate_expression(expression1)
    print(f"Expression: {expression1}, Result: {result1}")
    expression2 = "(3 + 4) * 2"
    result2 = evaluate_expression(expression2)
    print(f"Expression: {expression2}, Result: {result2}")
    expression3 = "10 / 2 + 5 * 3"
    result3 = evaluate_expression(expression3)
    print(f"Expression: {expression3}, Result: {result3}")
    expression4 = "10 - (4 + 2) * 3"
    result4 = evaluate_expression(expression4)
    print(f"Expression: {expression4}, Result: {result4}")
    expression5 = "100 / (5 * (8 - 4))"
    result5 = evaluate_expression(expression5)
    print(f"Expression: {expression5}, Result: {result5}")
    expression6 = "5 + 2 * (10 - 3) / 2"
    result6 = evaluate_expression(expression6)
    print(f"Expression: {expression6}, Result: {result6}")