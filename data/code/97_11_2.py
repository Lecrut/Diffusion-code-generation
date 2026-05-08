def generate_truth_table(a, b):
    print(f"a: {a}, b: {b}")
    print("--------------------")
    print("a | b | a AND b | a OR b | NOT a")
    print("---|---|---------|--------|-------")
    print(f"{a} | {b} | {a and b} | {a or b} | {not a}")
if __name__ == '__main__':
    generate_truth_table(True, True)
    print("\n" * 2)
    generate_truth_table(True, False)
    print("\n" * 2)
    generate_truth_table(False, True)
    print("\n" * 2)
    generate_truth_table(False, False)