def evaluate_boolean_expression(expression):
    def evaluate_token(token, vars):
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            return float(token)
        elif token in vars:
            return vars[token]
        raise NameError(f"Variable or undefined token: {token}")

    def parse_and_bind(tokens, vars):
        output_queue = []
        operator_stack = []
        precedence = {
            '==': 1, '!=': 1, '>': 2, '<': 2, '>=': 2, '<=': 2,
            'and': 3, 'or': 4, 'not': 5
        }

        def apply_op(op, values):
            if op == 'not':
                return not values[0]
            elif op == 'and':
                return all(values)
            elif op == 'or':
                return any(values)

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                output_queue.append(float(token))
            elif token in precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence[token] <= precedence[operator_stack[-1]]):
                    output_queue.append(apply_op(operator_stack.pop(), [output_queue.pop()]))
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(apply_op(operator_stack.pop(), [output_queue.pop()]))
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            i += 1

        while operator_stack:
            output_queue.append(apply_op(operator_stack.pop(), [output_queue.pop()]))

        return output_queue[0]

    tokens = expression.split()
    variables = {}
    for token in tokens:
        if '=' in token:
            key, value = token.split('=')
            variables[key.strip()] = evaluate_token(value.strip(), variables)

    return parse_and_bind(tokens, variables)

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False or not True"))
    print(evaluate_boolean_expression("not (False or True) and True"))
    print(evaluate_boolean_expression("True and not (False and True)"))
    print(evaluate_boolean_expression("(True or False) and (not False)"))