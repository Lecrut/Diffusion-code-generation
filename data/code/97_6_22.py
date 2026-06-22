def validate_inputs(inputs):
    if not isinstance(inputs, (list, tuple)):
        raise ValueError("Inputs must be a list or tuple of tuples.")
    for item in inputs:
        if not isinstance(item, (list, tuple)):
            raise ValueError("Each input item must be a tuple or list.")
        if len(item) != 2:
            raise ValueError("Each input tuple must contain exactly two values.")
        p, q = item
        if not isinstance(p, bool) or not isinstance(q, bool):
            raise ValueError("Input values must be boolean.")
    return True

def compute_logic(p, q):
    and_res = p and q
    or_res = p or q
    xor_res = p != q
    not_p = not p
    implies_res = (not p) or q
    return and_res, or_res, xor_res, not_p, implies_res

def format_row(p, q, and_res, or_res, xor_res, not_p, implies_res):
    col_width = 12
    p_str = str(p).center(col_width)
    q_str = str(q).center(col_width)
    and_str = str(and_res).center(col_width)
    or_str = str(or_res).center(col_width)
    xor_str = str(xor_res).center(col_width)
    not_p_str = str(not_p).center(col_width)
    implies_str = str(implies_res).center(col_width)
    return f"{p_str}|{q_str}|{and_str}|{or_str}|{xor_str}|{not_p_str}|{implies_str}"

def print_truth_table(inputs):
    validate_inputs(inputs)
    
    headers = ["P", "Q", "P AND Q", "P OR Q", "P XOR Q", "NOT P", "P IMPLIES Q"]
    col_width = 12
    header_line = "|".join(h.center(col_width) for h in headers)
    separator = "-" * len(header_line)
    
    print(header_line)
    print(separator)
    
    for p, q in inputs:
        and_res, or_res, xor_res, not_p, implies_res = compute_logic(p, q)
        print(format_row(p, q, and_res, or_res, xor_res, not_p, implies_res))

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)