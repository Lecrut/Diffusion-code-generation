def truth_table(expr1, expr2):
    import itertools
    vars = set(expr1) & set(expr2)
    if not vars:
        return expr1 == expr2
    truth_values = list(itertools.product([False, True], repeat=len(vars)))
    results1 = [eval(expr1, {'__builtins__': None}, {var: val}) for var, val in zip(vars, truth_values)]
    results2 = [eval(expr2, {'__builtins__': None}, {var: val}) for var, val in zip(vars, truth_values)]
    return results1 == results2
if __name__ == '__main__':
    expr1 = 'a and b'
    expr2 = 'b and a'
    print(truth_table(expr1, expr2))