TRUE = True
FALSE = False

def evaluate_logic(p, q):
    r = p ^ q
    return p and q or (not p and r)
if __name__ == '__main__':
    test_cases = [(TRUE, TRUE), (TRUE, FALSE), (FALSE, TRUE), (FALSE, FALSE)]
    results = {case: evaluate_logic(*case) for case in test_cases}
    print(results)