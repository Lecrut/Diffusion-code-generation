def evaluate_logic(p, q):
    r = p ^ q
    return (p and q) or ((not p) and r)

def run_tests():
    test_cases = {
        (True, True): "TT",
        (True, False): "TF",
        (False, True): "FT",
        (False, False): "FF"
    }
    results = {}
    for p, q in test_cases:
        results[(p, q)] = evaluate_logic(p, q)
    return results

if __name__ == '__main__':
    output = run_tests()
    print(output)