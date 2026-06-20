def generate_truth_table(a, b):
    print(f"A | B | A AND B")
    for a_val in [False, True]:
        for b_val in [False, True]:
            result = a_val and b_val
            print(f"{a_val} | {b_val} | {result}")

if __name__ == '__main__':
    generate_truth_table(True, False)