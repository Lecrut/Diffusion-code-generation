def generate_truth_table(booleans):
    if not all(isinstance(b, bool) for b in booleans):
        raise ValueError("All elements must be boolean values")

    num_vars = len(booleans)
    truth_table = []

    def generate_combinations(index=0, current_combo=[]):
        if index == num_vars:
            truth_table.append(current_combo[:])
            return
        for value in [False, True]:
            current_combo.append(value)
            generate_combinations(index + 1, current_combo)
            current_combo.pop()

    generate_combinations()
    return truth_table

if __name__ == '__main__':
    sample_booleans = [True, False]
    print(generate_truth_table(sample_booleans))