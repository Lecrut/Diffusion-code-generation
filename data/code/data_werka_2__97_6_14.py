def print_truth_table(inputs):
    if not inputs:
        print("P Q | P AND Q | P OR Q | P XOR Q | NOT P | NOT Q")
        print("- - | ------- | ------ | ------- | ----- | -----")
        return

    max_len = max(len(p) for p, q in inputs)
    header_p = "P"
    header_q = "Q"
    if max_len > 1:
        header_p = "P" * max_len
        header_q = "Q" * max_len

    print(f"{header_p} {header_q} | P AND Q | P OR Q | P XOR Q | NOT P | NOT Q")
    print("-" * len(header_p) + " " + "-" * len(header_q) + " | ------- | ------ | ------- | ----- | -----")

    for p_vals, q_vals in inputs:
        p_str = p_vals if len(p_vals) == max_len else p_vals + " " * (max_len - len(p_vals))
        q_str = q_vals if len(q_vals) == max_len else q_vals + " " * (max_len - len(q_vals))
        
        and_res = ''.join('1' if a and b else '0' for a, b in zip(p_vals, q_vals))
        or_res = ''.join('1' if a or b else '0' for a, b in zip(p_vals, q_vals))
        xor_res = ''.join('1' if a != b else '0' for a, b in zip(p_vals, q_vals))
        not_p = ''.join('0' if a == '1' else '1' for a in p_vals)
        not_q = ''.join('0' if b == '1' else '1' for b in q_vals)
        
        print(f"{p_str} {q_str} | {and_res}     | {or_res}    | {xor_res}     | {not_p}   | {not_q}   ")

if __name__ == '__main__':
    sample_inputs = [
        ("1", "1"),
        ("1", "0"),
        ("0", "1"),
        ("0", "0")
    ]
    print_truth_table(sample_inputs)