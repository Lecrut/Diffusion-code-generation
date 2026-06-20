def evaluate_boolean_expression(expression, variables):
    def parse_and_evaluate(tokens):
        stack = []
        current_token = ''
        for token in tokens:
            if token == '(':
                stack.append(current_token)
                current_token = ''
            elif token == ')':
                sub_expression = current_token + token
                while stack and stack[-1] != '(':
                    sub_expression = stack.pop() + sub_expression
                stack.pop()
                current_token = evaluate(sub_expression[1:-1])
            else:
                current_token += token
        return evaluate(current_token)

    def evaluate(expression):
        if expression.isdigit():
            return bool(int(expression))
        elif expression in variables:
            return variables[expression]
        elif ' and ' in expression:
            left, right = expression.split(' and ')
            return parse_and_evaluate(left.split()) and parse_and_evaluate(right.split())
        elif ' or ' in expression:
            left, right = expression.split(' or ')
            return parse_and_evaluate(left.split()) or parse_and_evaluate(right.split())

    tokens = ''.join(expression.split()).split()
    return parse_and_evaluate(tokens)

if __name__ == '__main__':
    variables = {'A': True, 'B': False, 'C': True}
    expression = '((A and B) or C)'
    result = evaluate_boolean_expression(expression, variables)
    print(result)