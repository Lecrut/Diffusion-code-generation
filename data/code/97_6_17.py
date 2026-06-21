def print_truth_table(inputs):
    if not inputs:
        return
    n = len(inputs[0])
    if n != 2:
        raise ValueError("Each tuple must contain exactly two values for P and Q")
    for p, q in inputs:
        p_val = bool(p)
        q_val = bool(q)
        and_res = p_val and q_val
        or_res = p_val or q_val
        xor_res = p_val ^ q_val
        nand_res = not (p_val and q_val)
        nor_res = not (p_val or q_val)
        impl_pq = (not p_val) or q_val
        impl_qp = (not q_val) or p_val
        equiv = p_val == q_val
        print(f"P={p_val}, Q={q_val} | P AND Q={and_res}, P OR Q={or_res}, P XOR Q={xor_res}, P NAND Q={nand_res}, P NOR Q={nor_res}, P -> Q={impl_pq}, Q -> P={impl_qp}, P <-> Q={equiv}")

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)