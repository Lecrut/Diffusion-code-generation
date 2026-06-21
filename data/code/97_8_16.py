def compute_logic_table(val_a, val_b):
    if not isinstance(val_a, bool) or not isinstance(val_b, bool):
        raise ValueError("Arguments must be booleans")
    ops = [
        ("a", lambda: val_a),
        ("b", lambda: val_b),
        ("a AND b", lambda: val_a and val_b),
        ("a OR b", lambda: val_a or val_b),
        ("a XOR b", lambda: val_a != val_b),
        ("NOT a", lambda: not val_a),
        ("NOT b", lambda: not val_b),
        ("a NAND b", lambda: not (val_a and val_b)),
        ("a NOR b", lambda: not (val_a or val_b)),
        ("a IMPLIES b", lambda: (not val_a) or val_b),
        ("b IMPLIES a", lambda: (not val_b) or val_a),
        ("a EQUIV b", lambda: val_a == val_b)
    ]
    return {name: func() for name, func in ops}

if __name__ == '__main__':
    output = compute_logic_table(True, False)
    print(output)