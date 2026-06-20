def evaluate_logic(p, q):
    r = p ^ q
    result = (p and q) or (not p and r)
    return result

if __name__ == '__main__':
    test_cases = [(True, False), (False, True), (True, True), (False, False)]
    results = {case: evaluate_logic(*case) for case in test_cases}
    print(results)