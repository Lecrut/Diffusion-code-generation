def print_truth_table(tuples):
    for p, q in tuples:
        print(f"P: {p}, Q: {q}")

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)