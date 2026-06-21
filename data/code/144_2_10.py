def evaluate_logical_equivalence():
    results = []
    for a in [False, True]:
        for b in [False, True]:
            xor_result = (a ^ b)
            not_and_result = (not a) and b
            results.append((a, b, xor_result == not_and_result))
    return results

if __name__ == '__main__':
    print(evaluate_logical_equivalence())