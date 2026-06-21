def evaluate_equivalence():
    results = []
    for A in [True, False]:
        for B in [True, False]:
            expr1 = (A ^ B)
            expr2 = (not A) and B
            results.append((A, B, expr1 == expr2))
    return results

if __name__ == '__main__':
    table = evaluate_equivalence()
    print(table)