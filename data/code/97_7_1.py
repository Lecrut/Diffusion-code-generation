def print_truth_table(input_tuples):
    if not input_tuples:
        return
    p_values = [t[0] for t in input_tuples]
    q_values = [t[1] for t in input_tuples]
    header = "P | Q | P AND Q | P OR Q | NOT P"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for p, q in zip(p_values, q_values):
        p_and_q = p and q
        p_or_q = p or q
        not_p = not p
        print(f"{p} | {q} | {p_and_q} | {p_or_q} | {not_p}")
    print("-" * len(header))
if __name__ == '__main__':
    sample_data = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_data)