def print_truth_table(input_tuples):
    if not input_tuples:
        return
    P_values = [t[0] for t in input_tuples]
    Q_values = [t[1] for t in input_tuples]
    header = "P | Q | P $\\land$ Q | P $\\lor$ Q | $\\neg$ P"
    print(header)
    print("-" * len(header))
    for p, q in zip(P_values, Q_values):
        p_and_q = p and q
        p_or_q = p or q
        not_p = not p
        print(f"{p} | {q} | {p_and_q} | {p_or_q} | {not_p}")
if __name__ == '__main__':
    sample_data = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_data)