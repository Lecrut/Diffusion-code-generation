def evaluate_logic(p, q):
    if not isinstance(p, bool) or not isinstance(q, bool):
        raise ValueError("Inputs must be boolean values.")
    
    r = p ^ q
    return (p and q) or (not p and r)

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {case: evaluate_logic(*case) for case in test_cases}
    print(results)