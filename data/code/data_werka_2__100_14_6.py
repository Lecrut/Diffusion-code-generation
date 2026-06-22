def evaluate_logic(p, q):
    if p is not True and p is not False:
        raise ValueError("p must be boolean")
    if q is not True and q is not False:
        raise ValueError("q must be boolean")
    r = p ^ q
    part_a = p and q
    part_b = (not p) and r
    return part_a or part_b

def main():
    cases = [(True, True), (True, False), (False, True), (False, False)]
    results = {}
    for p, q in cases:
        res = evaluate_logic(p, q)
        results[(p, q)] = res
    print(results)

if __name__ == '__main__':
    main()