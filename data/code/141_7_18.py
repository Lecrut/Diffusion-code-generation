def evaluate_expression(expression):
    precedence = {'AND': 2, 'OR': 1}
    operators = set(precedence.keys())

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'AND':
            values.append(left and right)
        elif operator == 'OR':
            values.append(left or right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    def evaluate(tokens):
        operators_stack = []
        values_stack = []
        for token in tokens:
            if token.isdigit():
                values_stack.append(int(token))
            elif token in operators:
                while operators_stack and operators_stack[-1] != '(' and greater_precedence(operators_stack[-1], token):
                    apply_operator(operators_stack, values_stack)
                operators_stack.append(token)
            elif token == '(':
                operators_stack.append(token)
            elif token == ')':
                while operators_stack[-1] != '(':
                    apply_operator(operators_stack, values_stack)
                operators_stack.pop()
        while operators_stack:
            apply_operator(operators_stack, values_stack)
        return values_stack[0]
    tokens = expression.replace(' ', '').split()
    return evaluate(tokens)
if __name__ == '__main__':
    result = evaluate_expression('1 AND 0 OR 1')
    print(result)