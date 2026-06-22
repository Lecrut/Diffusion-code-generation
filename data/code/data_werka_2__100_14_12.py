def evaluate_logic(p, q):
    if not isinstance(p, bool) or not isinstance(q, bool):
        raise ValueError("Inputs must be boolean")
    r = p ^ q
    term1 = p and q
    term2 = (not p) and r
    return term1 or term2

def run_tests():
    test_cases = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    results = {}
    for p, q in test_cases:
        val = evaluate_logic(p, q)
        results[(p, q)] = val
    return results

if __name__ == '__main__':
    output = run_tests()
    print(output)