def evaluate_logic(p, q):
    r = p ^ q
    return (p and q) or ((not p) and r)

if __name__ == '__main__':
    inputs = [(True, True), (True, False), (False, True), (False, False)]
    results = {}
    for p, q in inputs:
        results[(p, q)] = evaluate_logic(p, q)
    print(results)