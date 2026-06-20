import itertools

def evaluate_expression(expr, assignment):
    if isinstance(expr, bool):
        return expr
    elif isinstance(expr, str):
        return assignment[expr]
    else:
        op = expr[0]
        args = expr[1:]
        left = evaluate_expression(args[0], assignment)
        right = evaluate_expression(args[1], assignment)
        if op == 'and':
            return left and right
        elif op == 'or':
            return left or right
        elif op == 'not':
            return not left

def generate_assignments(variables):
    return list(itertools.product([True, False], repeat=len(variables)))

def check_equivalence(expr1, expr2):
    variables = set()
    def extract_variables(expression):
        if isinstance(expression, str) and expression.isalpha():
            variables.add(expression)
        elif isinstance(expression, list):
            for arg in expression[1:]:
                extract_variables(arg)
    extract_variables(expr1)
    extract_variables(expr2)
    
    assignments = generate_assignments(variables)
    for assignment in assignments:
        assignment_dict = dict(zip(variables, assignment))
        if evaluate_expression(expr1, assignment_dict) != evaluate_expression(expr2, assignment_dict):
            return False
    return True

if __name__ == '__main__':
    expr1 = ['and', 'P', ['not', 'Q']]
    expr2 = ['or', ['not', 'P'], 'Q']
    print(f"Test 1 (expr1 vs expr2): {check_equivalence(expr1, expr2)}")