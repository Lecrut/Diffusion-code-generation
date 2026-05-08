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
    output_stack = []
    operator_stack = []
    def apply_op():
        op = operator_stack.pop()
        right = values.pop()
        left = values.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            values.append(left / right)
    for token in tokens:
        if token.isdigit() or (token.replace('.', '', 1).isdigit()):
            output_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                apply_op()
            operator_stack.pop()
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        elif token in ('+', '-', '*', '/'):
            while (operator_stack and operator_stack[-1] in ('+', '-', '*', '/')) and \
                  (operator_stack[-1] not in ('(')):
                apply_op()
            operator_stack.append(token)
    while operator_stack:
        apply_op()
    return values[0] if values else 0
if __name__ == '__main__':
    expression1 = "3 + 4 * 2"
    result1 = evaluate_expression(expression1)
    print(f"Expression: {expression1}, Result: {result1}")
    expression2 = "(3 + 4) * 2"
    result2 = evaluate_expression(expression2)
    print(f"Expression: {expression2}, Result: {result2}")
    expression3 = "10 / 2 - 3 * 4"
    result3 = evaluate_expression(expression3)
    print(f"Expression: {expression3}, Result: {result3}")
    expression4 = "10 + 2 * (6 - 3) / 2"
    result4 = evaluate_expression(expression4)
    print(f"Expression: {expression4}, Result: {result4}")
    expression5 = "100 / (5 + 5)"
    result5 = evaluate_expression(expression5)
    print(f"Expression: {expression5}, Result: {result5}")