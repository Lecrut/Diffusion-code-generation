P_AND_Q = True
NOT_P_AND_R = False

def evaluate_logic(p, q):
    r = p ^ q
    return (p and q) or (not p and r)

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {case: evaluate_logic(*case) for case in test_cases}
    print(results)