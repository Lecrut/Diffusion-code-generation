import itertools
def evaluate_expression(expression, assignment):
    if not expression:
        return False
    if expression == 'True':
        return True
    if expression == 'False':
        return False
    parts = expression.split(' is ')
    if len(parts) == 2:
        left_expr = parts[0].strip()
        right_expr = parts[1].strip()
        left_val = assignment.get(left_expr, None)
        right_val = assignment.get(right_expr, None)
        if left_val is None or right_val is None:
            return None
        if left_expr == 'and':
            return left_val and right_val
        elif left_expr == 'or':
            return left_val or right_val
        elif left_expr == 'not':
            return not right_val
        elif left_expr == 'equal':
            return left_val == right_val
        else:
            return None
    return None
def check_contradictions(expressions):
    n = len(expressions)
    for i in range(n):
        for j in range(i + 1, n):
            expr1 = expressions[i]
            expr2 = expressions[j]
            if expr1 == 'True' and expr2 == 'False' or expr1 == 'False' and expr2 == 'True':
                return True
    return False
if __name__ == '__main__':
    sample_expressions_1 = ['True', 'False', 'True']
    result_1 = check_contradictions(sample_expressions_1)
    print(f"Sample 1: {result_1}")
    sample_expressions_2 = ['True', 'False']
    result_2 = check_contradictions(sample_expressions_2)
    print(f"Sample 2: {result_2}")
    sample_expressions_3 = ['True', 'True']
    result_3 = check_contradictions(sample_expressions_3)
    print(f"Sample 3: {result_3}")
    sample_expressions_4 = ['True', 'False', 'True', 'False']
    result_4 = check_contradictions(sample_expressions_4)
    print(f"Sample 4: {result_4}")
    sample_expressions_5 = ['True', 'True', 'True']
    result_5 = check_contradictions(sample_expressions_5)
    print(f"Sample 5: {result_5}")