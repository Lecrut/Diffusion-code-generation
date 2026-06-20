def evaluate_boolean_expression(expression):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    stack_operands = []
    stack_operators = []

    def apply_operator():
        operator = stack_operators.pop()
        right = stack_operands.pop()
        left = stack_operands.pop()
        if operator == 'NOT':
            stack_operands.append(not right)
        elif operator == 'AND':
            stack_operands.append(left and right)
        elif operator == 'OR':
            stack_operands.append(left or right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or token.lower() in ('true', 'false'):
            stack_operands.append(token.lower() == 'true')
        elif token in precedence:
            while (stack_operators and stack_operators[-1] != '(' and
                   greater_precedence(stack_operators[-1], token)):
                apply_operator()
            stack_operators.append(token)
        elif token == '(':
            stack_operators.append(token)
        elif token == ')':
            while stack_operators[-1] != '(':
                apply_operator()
            stack_operators.pop()

    while stack_operators:
        apply_operator()

    return stack_operands[0]

if __name__ == '__main__':
    print(evaluate_boolean_expression('NOT true AND false OR true'))