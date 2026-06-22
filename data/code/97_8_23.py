def compute_logic_table(first, second):
    if not isinstance(first, bool) or not isinstance(second, bool):
        raise ValueError("Inputs must be boolean")
    ops = [
        ("a", first),
        ("b", second),
        ("a AND b", first and second),
        ("a OR b", first or second),
        ("a XOR b", first != second),
        ("NOT a", not first),
        ("NOT b", not second),
        ("a IMPLIES b", (not first) or second),
        ("b IMPLIES a", (not second) or first),
        ("a NAND b", not (first and second)),
        ("a NOR b", not (first or second)),
        ("a XNOR b", first == second),
    ]
    return dict(ops)

if __name__ == '__main__':
    print(compute_logic_table(True, False))