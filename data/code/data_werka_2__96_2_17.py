import re
import ast
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    tokens = re.findall(r'\(|\)|and|or|[A-Za-z_][A-Za-z0-9_]*', expression)
    
    def parse_expr(index):
        left, index = parse_term(index)
        while index < len(tokens) and tokens[index] == 'or':
            index += 1
            right, index = parse_term(index)
            left = left or right
        return left, index

    def parse_term(index):
        left, index = parse_factor(index)
        while index < len(tokens) and tokens[index] == 'and':
            index += 1
            right, index = parse_factor(index)
            left = left and right
        return left, index

    def parse_factor(index):
        token = tokens[index]
        if token == '(':
            index += 1
            result, index = parse_expr(index)
            if index < len(tokens) and tokens[index] == ')':
                index += 1
            return result, index
        elif token == 'and' or token == 'or':
            raise ValueError(f"Unexpected operator {token}")
        else:
            if token in variables:
                return variables[token], index + 1
            else:
                raise ValueError(f"Undefined variable {token}")

    result, _ = parse_expr(0)
    return result

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_dict = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expr, vars_dict))