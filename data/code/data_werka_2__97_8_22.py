def truth_table(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    op_and = a and b
    op_or = a or b
    op_xor = a != b
    op_nand = not op_and
    op_nor = not op_or
    op_eq = a == b
    op_neq = a != b
    op_imp_a_b = (not a) or b
    op_imp_b_a = (not b) or a
    op_xnor = not op_xor
    results = {
        "inputs": {"a": a, "b": b},
        "AND": op_and,
        "OR": op_or,
        "XOR": op_xor,
        "NAND": op_nand,
        "NOR": op_nor,
        "XNOR": op_xnor,
        "A implies B": op_imp_a_b,
        "B implies A": op_imp_b_a,
        "A == B": op_eq,
        "A != B": op_neq
    }
    return results

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    computed_table = truth_table(sample_a, sample_b)
    print(computed_table)