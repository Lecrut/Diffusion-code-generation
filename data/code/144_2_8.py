def evaluate_logic_equivalence():
    results = []
    for a in [False, True]:
        for b in [False, True]:
            xor_result = (a or b) and not(a and b)
            and_not_result = not a and b
            results.append((a, b, xor_result == and_not_result))
    return results

if __name__ == '__main__':
    print(evaluate_logic_equivalence())