def evaluate_logic(p, q):
    r = p ^ q
    term1 = p and q
    term2 = (not p) and r
    return term1 or term2

if __name__ == '__main__':
    inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {}
    for p, q in inputs:
        results[(p, q)] = evaluate_logic(p, q)
    print(results)