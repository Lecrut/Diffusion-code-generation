R = lambda p, q: p ^ q

def evaluate_logic(p, q):
    r = R(p, q)
    return (p and q) or (not p and r)

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {case: evaluate_logic(*case) for case in test_cases}
    print(results)