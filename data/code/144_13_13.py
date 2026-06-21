from itertools import product

def evaluate_expression(assignments, expression):
    results = {}
    for assignment in assignments:
        P, Q = assignment
        try:
            result = eval(expression, {"__builtins__": None}, {"P": P, "Q": Q})
            results[assignment] = result
        except Exception:
            results[assignment] = False
    return results

if __name__ == '__main__':
    input_assignments = list(product([True, False], repeat=3))
    expression = "A or B and C"
    print(evaluate_expression(input_assignments, expression))