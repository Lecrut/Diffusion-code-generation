from enum import Enum

class Operator(Enum):
    AND = 'and'
    OR = 'or'
    NOT = 'not'

PRIORITY_AND = 2
PRIORITY_OR = 1

def evaluate_nested_conditions(a, b, c, d, e):
    expr_list = [a, Operator.AND, b, Operator.OR, c, Operator.AND, d, Operator.OR, e]
    
    def parse_expression(tokens, min_priority):
        left = parse_term(tokens)
        while tokens and isinstance(tokens[0], Operator) and _priority(tokens[0]) >= min_priority:
            op = tokens.pop(0)
            right = parse_term(tokens)
            if op == Operator.AND:
                left = left and right
            elif op == Operator.OR:
                left = left or right
        return left

    def parse_term(tokens):
        if isinstance(tokens[0], bool):
            return tokens.pop(0)
        if isinstance(tokens[0], Operator) and tokens[0] == Operator.NOT:
            tokens.pop(0)
            val = parse_term(tokens)
            return not val
        return parse_paren_group(tokens)

    def parse_paren_group(tokens):
        if not tokens:
            return False
        return parse_expression(tokens, PRIORITY_AND)

    def _priority(op):
        if op == Operator.AND:
            return PRIORITY_AND
        if op == Operator.OR:
            return PRIORITY_OR
        return 0

    work_tokens = list(expr_list)
    return parse_expression(work_tokens, PRIORITY_OR)

if __name__ == '__main__':
    res = evaluate_nested_conditions(True, False, True, False, True)
    print(res)