def print_truth_row(a, b):
    and_result = a and b
    or_result = a or b
    xor_result = a != b
    not_a = not a
    not_b = not b
    print(f"{a} | {b} | {and_result} | {or_result} | {xor_result} | {not_a} | {not_b}")

def validate_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")

def generate_truth_table(a, b):
    validate_inputs(a, b)
    print("A | B | A AND B | A OR B | A XOR B | NOT A | NOT B")
    for a_val in [True, False]:
        for b_val in [True, False]:
            print_truth_row(a_val, b_val)

if __name__ == '__main__':
    generate_truth_table(True, False)