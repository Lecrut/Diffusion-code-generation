def evaluate_boolean_expression(expression: str, variables: dict) -> bool:

    def parse_and_evaluate(tokens):
        stack = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(token)
            elif token in ['and', 'or']:
                stack.append(token)
            elif token == ')':
                sub_expr = []
                while stack and stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == 'and':
                    stack.append(all(parse_and_evaluate(sub_expr)))
                else:
                    stack.append(any(parse_and_evaluate(sub_expr)))
            elif token in variables:
                stack.append(variables[token])
            i += 1
        return stack[0]
    tokens = expression.replace(' ', '').split()
    return parse_and_evaluate(tokens)
if __name__ == '__main__':
    sample_expression = '((A and B) or C)'
    sample_variables = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(sample_expression, sample_variables))