def evaluate_logic(p, q):
    r = p ^ q
    if p and q:
        return True
    if not p:
        return r
    return False

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {}
    for p, q in test_cases:
        results[(p, q)] = evaluate_logic(p, q)
    print(results)