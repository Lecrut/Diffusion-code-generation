def truth_table(input_a, input_b):
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    
    op_and = input_a and input_b
    op_or = input_a or input_b
    op_xor = input_a ^ input_b
    op_nand = not op_and
    op_nor = not op_or
    op_implies_ab = (not input_a) or input_b
    op_implies_ba = (not input_b) or input_a
    op_equality = input_a == input_b
    
    return {
        "val_a": input_a,
        "val_b": input_b,
        "AND": op_and,
        "OR": op_or,
        "XOR": op_xor,
        "NAND": op_nand,
        "NOR": op_nor,
        "A implies B": op_implies_ab,
        "B implies A": op_implies_ba,
        "A == B": op_equality
    }

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    output = truth_table(sample_a, sample_b)
    print(output)