def evaluate_logic(p, q):
    r = p ^ q
    term1 = p and q
    term2 = (not p) and r
    return term1 or term2

def compute_results():
    test_cases = {
        (True, True): evaluate_logic(True, True),
        (True, False): evaluate_logic(True, False),
        (False, True): evaluate_logic(False, True),
        (False, False): evaluate_logic(False, False)
    }
    return test_cases

if __name__ == '__main__':
    output = compute_results()
    print(output)