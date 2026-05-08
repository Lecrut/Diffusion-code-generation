def generate_truth_table(a, b):
    results = {}
    combinations = [(a, b), (a, not b), (not a, b), (not a, not b)]
    for val_a, val_b in combinations:
        result = (val_a, val_b)
        if val_a and val_b:
            result_str = "T"
        elif val_a or val_b:
            result_str = "T"
        else:
            result_str = "F"
        key = f"A={val_a}, B={val_b}"
        results[key] = result_str
    return results
if __name__ == '__main__':
    input_a = True
    input_b = False
    truth_table = generate_truth_table(input_a, input_b)
    print(truth_table)