def calculate_implication_truth_table(list_p, list_q):
    truth_table = []
    for p, q in zip(list_p, list_q):
        result = not p or q
        truth_table.append((p, q, result))
    return truth_table
if __name__ == '__main__':
    p_values = [True, False, True, False]
    q_values = [True, True, False, False]
    result = calculate_implication_truth_table(p_values, q_values)
    for p, q, r in result:
        print(f"P: {p}, Q: {q}, P -> Q: {r}")