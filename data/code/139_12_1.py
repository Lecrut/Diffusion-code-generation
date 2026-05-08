def simulate_gates(a, b):
    and_result = a & b
    or_result = a | b
    not_a_result = 1 - a
    not_b_result = 1 - b
    not_a_and_b_result = 1 - (a & b)
    not_a_or_b_result = 1 - (a | b)
    return and_result, or_result, not_a_result, not_b_result
if __name__ == '__main__':
    input_a = 1
    input_b = 0
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    and_out, or_out, not_a, not_b = simulate_gates(input_a, input_b)
    print("--- Results ---")
    print(f"AND ({input_a} AND {input_b}): {and_out}")
    print(f"OR ({input_a} OR {input_b}): {or_out}")
    print(f"NOT A (NOT {input_a}): {not_a}")
    print(f"NOT B (NOT {input_b}): {not_b}")