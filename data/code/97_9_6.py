def generate_truth_table(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    
    headers = ["A", "B", "NOT A", "NOT B", "A AND B", "A OR B", "A XOR B"]
    print(" | ".join(headers))
    
    for a_val in [True, False]:
        for b_val in [True, False]:
            not_a = not a_val
            not_b = not b_val
            and_result = a_val and b_val
            or_result = a_val or b_val
            xor_result = a_val != b_val
            print(f"{a_val} | {b_val} | {not_a} | {not_b} | {and_result} | {or_result} | {xor_result}")

if __name__ == '__main__':
    generate_truth_table(True, False)