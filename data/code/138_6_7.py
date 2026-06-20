def truth_table():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            implication = not A or B
            equivalence = A == B
            results.append((A, B, implication, equivalence))
    return results

if __name__ == '__main__':
    table = truth_table()
    print(table)