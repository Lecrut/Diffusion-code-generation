def print_truth_table(inputs):
    if not inputs:
        return
    p_vals = [item[0] for item in inputs]
    q_vals = [item[1] for item in inputs]
    print("P\tQ\tP AND Q\tP OR Q\tP XOR Q\tNOT P\tNOT Q")
    print("-" * 50)
    for p, q in zip(p_vals, q_vals):
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p != q
        not_p = not p
        not_q = not q
        print(f"{p}\t{q}\t{p_and_q}\t{p_or_q}\t{p_xor_q}\t{not_p}\t{not_q}")

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_inputs)