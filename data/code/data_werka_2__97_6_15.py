def print_truth_table(inputs):
    if not inputs:
        print("P Q | P AND Q | P OR Q | P XOR Q | NOT P | NOT Q")
        print("- - | --------- | -------- | --------- | ----- | -----")
        return

    results = []
    for p, q in inputs:
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p ^ q
        not_p = not p
        not_q = not q
        results.append((p, q, p_and_q, p_or_q, p_xor_q, not_p, not_q))

    header = "P Q | P AND Q | P OR Q | P XOR Q | NOT P | NOT Q"
    separator = "- - | --------- | -------- | --------- | ----- | -----"
    print(header)
    print(separator)
    for p, q, p_and_q, p_or_q, p_xor_q, not_p, not_q in results:
        p_str = str(p).upper()
        q_str = str(q).upper()
        p_and_q_str = str(p_and_q).upper()
        p_or_q_str = str(p_or_q).upper()
        p_xor_q_str = str(p_xor_q).upper()
        not_p_str = str(not_p).upper()
        not_q_str = str(not_q).upper()
        print(f"{p_str} {q_str} | {p_and_q_str}     | {p_or_q_str}   | {p_xor_q_str}     | {not_p_str}   | {not_q_str}   ")

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_inputs)