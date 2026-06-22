def evaluate_logic(p, q):
    r = p ^ q
    term1 = p and q
    term2 = (not p) and r
    return term1 or term2

def main():
    inputs = {
        "case1": (True, True),
        "case2": (True, False),
        "case3": (False, True),
        "case4": (False, False)
    }
    results = {}
    for label, (p, q) in inputs.items():
        results[label] = evaluate_logic(p, q)
    print(results)

if __name__ == '__main__':
    main()