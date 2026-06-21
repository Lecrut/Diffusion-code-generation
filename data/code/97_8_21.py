def compute_logic_table(val_a, val_b):
    if not isinstance(val_a, bool) or not isinstance(val_b, bool):
        raise ValueError("Inputs must be boolean")
    op_and = val_a and val_b
    op_or = val_a or val_b
    op_xor = val_a ^ val_b
    op_nand = not op_and
    op_nor = not op_or
    op_eq = val_a == val_b
    op_neq = val_a != val_b
    op_imp_ab = (not val_a) or val_b
    op_imp_ba = (not val_b) or val_a
    return {
        "A": val_a,
        "B": val_b,
        "A AND B": op_and,
        "A OR B": op_or,
        "A XOR B": op_xor,
        "A NAND B": op_nand,
        "A NOR B": op_nor,
        "A == B": op_eq,
        "A != B": op_neq,
        "A -> B": op_imp_ab,
        "B -> A": op_imp_ba
    }

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    output = compute_logic_table(sample_a, sample_b)
    print(output)