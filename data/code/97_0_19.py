def print_truth_table(p_val, q_val):
    p = bool(p_val)
    q = bool(q_val)
    p_and_q = p and q
    p_or_q = p or q
    not_p = not p
    not_q = not q
    return f"{p} | {q} | {p_and_q} | {p_or_q} | {not_p} | {not_q}"

if __name__ == '__main__':
    samples = [(True, True), (True, False), (False, True), (False, False)]
    for p_val, q_val in samples:
        print(print_truth_table(p_val, q_val))