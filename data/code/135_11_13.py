def truth_values(num_vars):
    return list(itertools.product([True, False], repeat=num_vars))

def evaluate(expr, assignment):
    for var, value in zip(expr['vars'], assignment):
        expr['expr'] = expr['expr'].replace(var, str(value))
    return eval(expr['expr'])

def check_equivalence(expr1, expr2):
    if 'vars' not in expr1 or 'vars' not in expr2:
        raise ValueError("Expressions must have a 'vars' key and an 'expr' key.")
    if set(expr1['vars']) != set(expr2['vars']):
        return False
    for assignment in truth_values(len(expr1['vars'])):
        if evaluate(expr1, assignment) != evaluate(expr2, assignment):
            return False
    return True
if __name__ == '__main__':
    expr_a = {'vars': ['p', 'q'], 'expr': '(p and q)'}
    expr_b = {'vars': ['p', 'q'], 'expr': '(q and p)'}
    print(f'Test 1: {check_equivalence(expr_a, expr_b)}')
    expr_c = {'vars': ['p'], 'expr': 'p'}
    expr_d = {'vars': ['p'], 'expr': 'not p'}
    print(f'Test 2: {check_equivalence(expr_c, expr_d)}')