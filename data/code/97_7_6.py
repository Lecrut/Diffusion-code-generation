def print_truth_table(input_tuples):
    if not input_tuples:
        return
    P_values = [t[0] for t in input_tuples]
    Q_values = [t[1] for t in input_tuples]
    header = "P | Q | P AND Q | P OR Q | NOT P"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for p, q in zip(P_values, Q_values):
        p_and_q = "T" if p and q else "F"
        p_or_q = "T" if p or q else "F"
        not_p = "T" if not p else "F"
        print(f"{p} | {q} | {p_and_q} | {p_or_q} | {not_p}")
if __name__ == '__main__':
    sample_data = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_data)