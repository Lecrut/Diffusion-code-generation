def truth_table_eval(expr, vars):
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    results = []
    for a, b in inputs:
        result1 = eval(expr, {"__builtins__": None}, {**vars, "a": a, "b": b})
        results.append(result1)
    return all(results) and len(set(results)) == 1

def are_logically_equivalent(expr1, expr2):
    truth_values = [False, True]
    vars = {'A': truth_values, 'B': truth_values}
    expr1_eval = lambda: eval(expr1, {"__builtins__": None}, vars)
    expr2_eval = lambda: eval(expr2, {"__builtins__": None}, vars)
    return truth_table_eval(expr1, vars) == truth_table_eval(expr2, vars)

if __name__ == '__main__':
    expression1 = "A and B"
    expression2 = "(A and B)"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression1, expression2)}")