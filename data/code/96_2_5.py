def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    def parse_and_eval(tokens):
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
                current_token = eval(sub_expr, variables)
            else:
                current_token += token
        return eval(current_token, variables)

    tokens = expression.replace(' ', '').split()
    return parse_and_eval(tokens)

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars_dict)
    print(result)