def print_truth_table(a, b):
    print(f"a: {a}, b: {b}")
    print(f"True, True")
    print(f"True, False")
    print(f"False, True")
    print(f"False, False")
if __name__ == '__main__':
    print_truth_table(True, True)
    print("-" * 10)
    print_truth_table(True, False)
    print("-" * 10)
    print_truth_table(False, True)
    print("-" * 10)
    print_truth_table(False, False)