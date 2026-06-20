def generate_truth_table(input_tuples):
    print("Truth Table for P, Q")
    for p, q in input_tuples:
        print(f"P={p}, Q={q}")

if __name__ == '__main__':
    sample_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    generate_truth_table(sample_inputs)