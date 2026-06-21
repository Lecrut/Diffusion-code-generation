def evaluate_equivalence():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            xor_result = A ^ B
            and_not_a_b = not A and B
            results.append((A, B, xor_result, and_not_a_b))
    return results

if __name__ == '__main__':
    equivalence_table = evaluate_equivalence()
    for row in equivalence_table:
        print(row)