def check_contradictions(expr1, expr2):
    n = len(expr1)
    for i in range(2**n):
        truth_values = [bool(i >> j & 1) for j in range(n)]
        if eval(expr1, {'__builtins__': None}, dict(zip('pqr', truth_values))) != \
           eval(expr2, {'__builtins__': None}, dict(zip('pqr', truth_values))):
            return True
    return False

if __name__ == '__main__':
    expr1 = 'p and not q'
    expr2 = 'q or not p'
    print(check_contradictions(expr1, expr2))