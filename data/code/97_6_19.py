def print_truth_table(inputs):
    if not inputs:
        return
    p_values = [row[0] for row in inputs]
    q_values = [row[1] for row in inputs]
    print("P\tQ\tP AND Q\tP OR Q\tP XOR Q\tP IMPLIES Q")
    for p, q in zip(p_values, q_values):
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p != q
        p_implies_q = (not p) or q
        p_str = str(p)
        q_str = str(q)
        and_str = str(p_and_q)
        or_str = str(p_or_q)
        xor_str = str(p_xor_q)
        implies_str = str(p_implies_q)
        print(f"{p_str}\t{q_str}\t{and_str}\t{or_str}\t{xor_str}\t{implies_str}")

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)