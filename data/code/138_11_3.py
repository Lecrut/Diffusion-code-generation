def generate_truth_table(a, b):
    results = {}
    combinations = [(a, b), (False, True), (True, False)]
    for val_a, val_b in combinations:
        result = (val_a and val_b)
        key = (val_a, val_b)
        results[key] = result
    return results
if __name__ == '__main__':
    a_val = False
    b_val = False
    truth_table = generate_truth_table(a_val, b_val)
    print(truth_table)