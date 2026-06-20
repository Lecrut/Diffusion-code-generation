def evaluate_boolean_expression(expression: str, variables: dict) -> bool:

    def parse_and_eval(tokens):
        if len(tokens) == 1:
            return tokens[0]
        operator = tokens.pop()
        left = parse_and_eval(tokens)
        right = parse_and_eval(tokens)
        if operator == 'and':
            return left and right
        elif operator == 'or':
            return left or right
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in (' ', ')'):
            i += 1
        elif expression[i] == '(':
            tokens.append('(')
            i += 1
        elif expression[i].isalpha():
            j = i + 1
            while j < len(expression) and expression[j].isalpha():
                j += 1
            tokens.append(variables[expression[i:j]])
            i = j
        else:
            operator = expression[i]
            tokens.append(operator)
            i += 1
    return parse_and_eval(tokens)
if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars_dict)
    print(result)