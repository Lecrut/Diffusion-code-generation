import re
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    tokens = tokenize(expression)
    result, _ = parse_or(tokens, 0)
    return result

def tokenize(expression: str):
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression = re.sub(r'\band\b', ' and ', expression)
    expression = re.sub(r'\bor\b', ' or ', expression)
    expression = re.sub(r'\bnot\b', ' not ', expression)
    tokens = expression.split()
    return [t for t in tokens if t]

def parse_or(tokens, index):
    left, index = parse_and(tokens, index)
    while index < len(tokens) and tokens[index] == 'or':
        index += 1
        right, index = parse_and(tokens, index)
        left = left or right
    return left, index

def parse_and(tokens, index):
    left, index = parse_not(tokens, index)
    while index < len(tokens) and tokens[index] == 'and':
        index += 1
        right, index = parse_not(tokens, index)
        left = left and right
    return left, index

def parse_not(tokens, index):
    if index < len(tokens) and tokens[index] == 'not':
        index += 1
        val, index = parse_not(tokens, index)
        return not val, index
    return parse_primary(tokens, index)

def parse_primary(tokens, index):
    if index >= len(tokens):
        raise ValueError("Unexpected end of expression")
    token = tokens[index]
    if token == '(':
        index += 1
        val, index = parse_or(tokens, index)
        if index >= len(tokens) or tokens[index] != ')':
            raise ValueError("Missing closing parenthesis")
        index += 1
        return val, index
    if token == 'True':
        return True, index + 1
    if token == 'False':
        return False, index + 1
    if token in variables:
        val = variables[token]
        if not isinstance(val, bool):
            raise ValueError(f"Variable {token} is not a boolean")
        return val, index + 1
    raise ValueError(f"Unknown token: {token}")

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars_dict)
    print(result)