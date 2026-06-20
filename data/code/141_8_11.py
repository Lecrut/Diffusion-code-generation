def compute_logic_gates(a, b, c):
    return a & b, a | b, not a

if __name__ == '__main__':
    results = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                and_result, or_result, not_a = compute_logic_gates(a, b, c)
                results.append((a, b, c, and_result, or_result, not_a))
    print(results)