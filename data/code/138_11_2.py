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
        results[f"({val_a}, {val_b})"] = result
    return results
if __name__ == '__main__':
    a_val = True
    b_val = False
    truth_table = generate_truth_table(a_val, b_val)
    print(truth_table)