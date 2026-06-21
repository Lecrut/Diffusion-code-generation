def print_truth_table(inputs):
    if not inputs:
        return
    p_values = [item[0] for item in inputs]
    q_values = [item[1] for item in inputs]
    header = "P\tQ\tP AND Q\tP OR Q\tP XOR Q\tNOT P\tNOT Q"
    print(header)
    print("-" * len(header))
    for p, q in inputs:
        and_res = p and q
        or_res = p or q
        xor_res = p != q
        not_p = not p
        not_q = not q
        row = f"{str(p)}\t{str(q)}\t{str(and_res)}\t{str(or_res)}\t{str(xor_res)}\t{str(not_p)}\t{str(not_q)}"
        print(row)

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)