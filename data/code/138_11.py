def generate_truth_table(a, b):
    results = {}
    combinations = [(a, b)]
    for val_a, val_b in combinations:
        result = {
            "A": val_a,
            "B": val_b,
            "AND": val_a and val_b,
            "OR": val_a or val_b,
            "XOR": val_a ^ val_b,
            "NOT_A": not val_a,
            "NOT_B": not val_b
        }
        results[f"A={val_a}, B={val_b}"] = result
    return results
if __name__ == '__main__':
    input_a = False
    input_b = True
    truth_table = generate_truth_table(input_a, input_b)
    print(truth_table)