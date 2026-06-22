import re
from typing import Dict, Any

def evaluate_boolean_expression(expression: str, variables: Dict[str, bool]) -> bool:
    def parse_expression(tokens, pos):
        left, pos = parse_or(tokens, pos)
        return left, pos

    def parse_or(tokens, pos):
        left, pos = parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'or':
            pos += 1
            right, pos = parse_and(tokens, pos)
            left = left or right
        return left, pos

    def parse_and(tokens, pos):
        left, pos = parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'and':
            pos += 1
            right, pos = parse_not(tokens, pos)
            left = left and right
        return left, pos

    def parse_not(tokens, pos):
        if pos < len(tokens) and tokens[pos] == 'not':
            pos += 1
            val, pos = parse_not(tokens, pos)
            return not val, pos
        return parse_primary(tokens, pos)

    def parse_primary(tokens, pos):
        if pos < len(tokens) and tokens[pos] == '(':
            pos += 1
            val, pos = parse_expression(tokens, pos)
            if pos < len(tokens) and tokens[pos] == ')':
                pos += 1
            return val, pos
        if pos < len(tokens):
            token = tokens[pos]
            if token in ('True', 'False'):
                return token == 'True', pos + 1
            if token in variables:
                return variables[token], pos + 1
            raise ValueError(f"Unknown token: {token}")
        raise ValueError("Unexpected end of expression")

    tokens = re.findall(r'\(|\)|and|or|not|True|False|\w+', expression)
    result, _ = parse_expression(tokens, 0)
    return result

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expr, vars_dict))