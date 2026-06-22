def print_truth_table(inputs):
    if not inputs:
        return
    headers = ["P", "Q", "P AND Q", "P OR Q", "P XOR Q", "NOT P", "P IMPLIES Q"]
    print(" | ".join(headers))
    print("-" * (len(headers) * 7 - 1))
    for p, q in inputs:
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p != q
        not_p = not p
        p_implies_q = (not p) or q
        row = [
            str(p),
            str(q),
            str(p_and_q),
            str(p_or_q),
            str(p_xor_q),
            str(not_p),
            str(p_implies_q)
        ]
        print(" | ".join(row))

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)