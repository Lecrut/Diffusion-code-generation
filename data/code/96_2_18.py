def evaluate_boolean_expression(expression: str, variables: dict) -> bool:

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
                stack.append(evaluate(sub_expr, variables))
                current_token = ''
            elif token in ['and', 'or']:
                if current_token:
                    stack.append(current_token)
                    current_token = ''
                stack.append(token)
            else:
                current_token += token
        if current_token:
            stack.append(current_token)
        return evaluate(' '.join(stack), variables)

    def evaluate(expression: str, variables: dict) -> bool:
        parts = expression.split()
        result = variables[parts[0]]
        i = 1
        while i < len(parts):
            operator = parts[i]
            operand = variables[parts[i + 1]]
            if operator == 'and':
                result &= operand
            elif operator == 'or':
                result |= operand
            i += 2
        return result
    tokens = expression.replace('(', '( ').replace(')', ' )').split()
    return parse_and_evaluate(tokens)
if __name__ == '__main__':
    sample_expression = '((A and B) or C)'
    sample_variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(sample_expression, sample_variables))