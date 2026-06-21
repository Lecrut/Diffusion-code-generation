def evaluate_logic(p, q):
    r = p ^ q
    if p and q:
        return True
    if not p and r:
        return True
    return False

if __name__ == '__main__':
    inputs = [(True, True), (True, False), (False, True), (False, False)]
    results = {}
    for p, q in inputs:
        results[(p, q)] = evaluate_logic(p, q)
    print(results)