def compute_logic_gates(a, b, c):
    and_result = a and b and c
    or_result = a or b or c
    not_a = not a
    not_b = not b
    not_c = not c
    return (and_result, or_result, not_a, not_b, not_c)
if __name__ == '__main__':
    results = compute_logic_gates(True, True, False)
    print(results)