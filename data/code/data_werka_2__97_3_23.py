def evaluate_implication(p, q):
    return (not p) or q

def collect_truth_rows():
    truth_values = [False, True]
    row_data = []
    for var_p in truth_values:
        for var_q in truth_values:
            res = evaluate_implication(var_p, var_q)
            row_data.append((var_p, var_q, res))
    return row_data

def display_table(data):
    for p_val, q_val, imp_val in data:
        print(f"P={p_val}, Q={q_val}, P -> Q={imp_val}")

if __name__ == '__main__':
    results = collect_truth_rows()
    display_table(results)