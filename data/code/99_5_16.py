OPERATORS_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}

def calculate_expression(operands, operators):
    def apply_operator(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b

    stack_operands = []
    stack_operators = []

    for i, operator in enumerate(operators):
        while stack_operators and OPERATORS_PRIORITY[stack_operators[-1]] >= OPERATORS_PRIORITY[operator]:
            right = stack_operands.pop()
            left = stack_operands.pop()
            op = stack_operators.pop()
            stack_operands.append(apply_operator(op, left, right))
        stack_operators.append(operator)
        stack_operands.append(operands[i])

    while stack_operators:
        right = stack_operands.pop()
        left = stack_operands.pop()
        op = stack_operators.pop()
        stack_operands.append(apply_operator(op, left, right))

    return stack_operands[0]

if __name__ == '__main__':
    operands = [2, 3, 4, 5]
    operators = ['+', '*', '-']
    print(calculate_expression(operands, operators))