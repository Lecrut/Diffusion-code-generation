def evaluate_logical_equivalence():
    results = []
    for a in [False, True]:
        for b in [False, True]:
            expr1 = (a ^ b)
            expr2 = (not a) and b
            results.append((a, b, expr1 == expr2))
    return results

if __name__ == '__main__':
    print(evaluate_logical_equivalence())