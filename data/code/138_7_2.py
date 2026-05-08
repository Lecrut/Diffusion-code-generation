def calculate_implication_truth_table(list_p, list_q):
    truth_table = []
    for p, q in zip(list_p, list_q):
        result = not p or q
        truth_table.append((p, q, result))
    return truth_table
if __name__ == '__main__':
    P_values = [True, False, True, False]
    Q_values = [True, True, False, False]
    result = calculate_implication_truth_table(P_values, Q_values)
    for p, q, r in result:
        print(f"P={p}, Q={q} => P -> Q is {r}")