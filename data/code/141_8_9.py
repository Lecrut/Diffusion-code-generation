def compute_logic_gates(a, b, c):
    and_result = a and b and c
    or_result = a or b or c
    not_a = not a
    not_b = not b
    not_c = not c
    return and_result, or_result, not_a, not_b, not_c

if __name__ == '__main__':
    sample_values = [(True, True, True), (True, True, False), (True, False, True), (True, False, False),
                     (False, True, True), (False, True, False), (False, False, True), (False, False, False)]
    for values in sample_values:
        and_result, or_result, not_a, not_b, not_c = compute_logic_gates(*values)
        print(f"Inputs: {values} -> AND: {and_result}, OR: {or_result}, NOT A: {not_a}, NOT B: {not_b}, NOT C: {not_c}")