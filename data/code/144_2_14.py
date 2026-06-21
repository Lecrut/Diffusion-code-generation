def evaluate_logical_equivalence():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            expr1 = (A ^ B)
            expr2 = (not A) and B
            results.append((A, B, expr1 == expr2))
    return results

if __name__ == '__main__':
    print(evaluate_logical_equivalence())