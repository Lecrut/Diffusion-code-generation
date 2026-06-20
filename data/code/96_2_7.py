def evaluate_expression(expression, variables):
    def parse_and_evaluate(tokens):
        stack = []
        current_token = ''
        for token in tokens:
            if token == '(':
                stack.append(current_token)
                current_token = ''
            elif token == ')':
                subexpression = current_token + ' ' + token
                while stack and stack[-1] != '(':
                    subexpression = stack.pop() + ' ' + subexpression
                stack.pop()
                current_token = evaluate_expression(subexpression, variables)
            else:
                current_token += token
        return eval(current_token)

    tokens = expression.replace('and', '&').replace('or', '|').split()
    return parse_and_evaluate(tokens)

if __name__ == '__main__':
    expression = '((A and B) or C)'
    variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_expression(expression, variables))