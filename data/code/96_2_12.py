def evaluate_boolean_expression(expression, variables):
    def parse_and_evaluate(tokens):
        stack = []
        current_token = ''
        for token in tokens:
            if token == '(':
                stack.append(current_token)
                current_token = ''
            elif token == ')':
                sub_expr = current_token + token
                while stack and stack[-1] != '(':
                    sub_expr = stack.pop() + sub_expr
                stack.pop()
                current_token = evaluate(sub_expr[1:-1])
            else:
                current_token += token
        return evaluate(current_token)

    def evaluate(expression):
        if 'and' in expression:
            left, right = expression.split(' and ')
            return parse_and_evaluate(left) and parse_and_evaluate(right)
        elif 'or' in expression:
            left, right = expression.split(' or ')
            return parse_and_evaluate(left) or parse_and_evaluate(right)
        else:
            return variables[expression]

    tokens = ''.join(expression.split()).split()
    return parse_and_evaluate(tokens)

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expr, vars))