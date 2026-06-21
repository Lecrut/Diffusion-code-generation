def evaluate_logical_equivalence():
    results = []
    for a in [True, False]:
        for b in [True, False]:
            expr1 = (a ^ b)
            expr2 = (not a) and b
            results.append((expr1, expr2))
    return results

if __name__ == '__main__':
    print(evaluate_logical_equivalence())