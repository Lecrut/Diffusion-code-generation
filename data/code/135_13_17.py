def evaluate_expression(expression):
    TRUE = 'True'
    FALSE = 'False'
    AND = 'and'
    OR = 'or'
    NOT = 'not'

    def parse_and_reduce(expr, context):
        parts = expr.split(AND)
        return all(parse_and_reduce(part.strip(), context) for part in parts)

    def parse_or_reduce(expr, context):
        parts = expr.split(OR)
        return any(parse_or_reduce(part.strip(), context) for part in parts)

    def parse_not_reduce(expr, context):
        inner_expr = expr.replace(NOT, '', 1).strip()
        return not parse_expression(inner_expr, context)

    if expression == TRUE:
        return True
    elif expression == FALSE:
        return False
    elif AND in expression:
        return parse_and_reduce(expression, {})
    elif OR in expression:
        return parse_or_reduce(expression, {})
    elif NOT in expression:
        return parse_not_reduce(expression, {})
    else:
        return context.get(expression, None)

def are_equivalent(expr1, expr2):
    truth_table_1 = {i: evaluate_expression(expr1, {f'p{i}': i % 2 == 0}) for i in range(4)}
    truth_table_2 = {i: evaluate_expression(expr2, {f'q{i}': i % 2 == 0}) for i in range(4)}
    return truth_table_1 == truth_table_2

if __name__ == '__main__':
    print(are_equivalent('p0 and p1', 'p1'))
    print(are_equivalent('p0 or p1', 'not (p0 and not p1)'))
    print(are_equivalent('not (p0 and p1)', '(not p0) or (not p1)'))