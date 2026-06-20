def validate_truth_table():
    A_values = [0, 1]
    B_values = [0, 1]
    print("A | B | (A AND B) OR (NOT A AND NOT B)")
    print("-" * 45)
    for a in A_values:
        for b in B_values:
            and_ab = a and b
            not_a_and_not_b = not a and not b
            result = and_ab or not_a_and_not_b
            print(f"{a} | {b} | {result}")

if __name__ == '__main__':
    validate_truth_table()