import re
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    tokens = tokenize(expression)
    result, _ = parse_or(tokens, 0)
    return result

def tokenize(expression: str):
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression = expression.replace('and', ' and ').replace('or', ' or ')
    expression = expression.replace('not', ' not ')
    parts = expression.split()
    tokens = []
    for part in parts:
        if part:
            tokens.append(part)
    return tokens

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
        if index < len(tokens) and tokens[index] == ')':
            index += 1
        else:
            raise ValueError("Missing closing parenthesis")
        return val, index
    elif token == 'True':
        return True, index + 1
    elif token == 'False':
        return False, index + 1
    else:
        if token in variables:
            return variables[token], index + 1
        else:
            raise ValueError(f"Unknown variable: {token}")

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars_dict)
    print(result)