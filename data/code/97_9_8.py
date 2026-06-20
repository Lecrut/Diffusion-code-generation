def generate_truth_table(a, b):
    print(f"A | B | A AND B")
    for a_val in [True, False]:
        for b_val in [True, False]:
            print(f"{a_val} | {b_val} | {a_val and b_val}")

if __name__ == '__main__':
    generate_truth_table(True, False)