import re
import operator

def evaluate_expression(expression: str, variables: dict) -> bool:
    tokens = tokenize(expression)
    result, _ = parse_or(tokens, 0)
    return result

def tokenize(expression: str) -> list:
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression = re.sub(r'\band\b', ' and ', expression)
    expression = re.sub(r'\bor\b', ' or ', expression)
    expression = re.sub(r'\bnot\b', ' not ', expression)
    tokens = expression.split()
    return [t for t in tokens if t]

def parse_or(tokens: list, pos: int):
    left, pos = parse_and(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'or':
        pos += 1
        right, pos = parse_and(tokens, pos)
        left = left or right
    return left, pos

def parse_and(tokens: list, pos: int):
    left, pos = parse_not(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'and':
        pos += 1
        right, pos = parse_not(tokens, pos)
        left = left and right
    return left, pos

def parse_not(tokens: list, pos: int):
    if pos < len(tokens) and tokens[pos] == 'not':
        pos += 1
        val, pos = parse_not(tokens, pos)
        return not val, pos
    return parse_primary(tokens, pos)

def parse_primary(tokens: list, pos: int):
    if pos >= len(tokens):
        raise ValueError("Unexpected end of expression")
    token = tokens[pos]
    if token == '(':
        pos += 1
        val, pos = parse_or(tokens, pos)
        if pos >= len(tokens) or tokens[pos] != ')':
            raise ValueError("Missing closing parenthesis")
        pos += 1
        return val, pos
    if token == 'true':
        return True, pos + 1
    if token == 'false':
        return False, pos + 1
    if token in variables:
        return variables[token], pos + 1
    raise ValueError(f"Unknown token: {token}")

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    print(evaluate_expression(expr, vars_dict))