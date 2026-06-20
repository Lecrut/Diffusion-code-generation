def generate_truth_table(a, b):
    print(f"A | B | A AND B | A OR B | A XOR B | NOT A | NOT B")
    for a_val in [True, False]:
        for b_val in [True, False]:
            and_result = a_val and b_val
            or_result = a_val or b_val
            xor_result = a_val != b_val
            not_a = not a_val
            not_b = not b_val
            print(f"{a_val} | {b_val} | {and_result} | {or_result} | {xor_result} | {not_a} | {not_b}")

if __name__ == '__main__':
    generate_truth_table(True, False)