def print_truth_table(input_tuples):
    if not input_tuples:
        return
    p_values = [t[0] for t in input_tuples]
    q_values = [t[1] for t in input_tuples]
    header = "P | Q | P AND Q | P OR Q | P XOR Q\n"
    print(header)
    for p, q in zip(p_values, q_values):
        p_and_q = "T" if p and q else "F"
        p_or_q = "T" if p or q else "F"
        p_xor_q = "T" if p != q else "F"
        print(f"{p} | {q} | {p_and_q} | {p_or_q} | {p_xor_q}")
if __name__ == '__main__':
    sample_data = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_data)