def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool):
        raise ValueError("First argument must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("Second argument must be a boolean")
    
    columns = ["A", "B", "AND", "OR", "XOR", "NAND", "NOR", "IMP"]
    headers = [col for col in columns]
    
    def get_logical_op(op_type, val_a, val_b):
        if op_type == "AND":
            return val_a and val_b
        if op_type == "OR":
            return val_a or val_b
        if op_type == "XOR":
            return val_a != val_b
        if op_type == "NAND":
            return not (val_a and val_b)
        if op_type == "NOR":
            return not (val_a or val_b)
        if op_type == "IMP":
            return (not val_a) or val_b
        return False

    table = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            row = [val_a, val_b]
            for op in ["AND", "OR", "XOR", "NAND", "NOR", "IMP"]:
                row.append(get_logical_op(op, val_a, val_b))
            table.append(row)
            
    return table

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    table = generate_truth_table(sample_a, sample_b)
    header_str = "A     B     AND     OR    XOR   NAND  NOR   IMP  "
    print(header_str)
    print("-" * 55)
    for row in table:
        row_str = ""
        for i, val in enumerate(row):
            if i < 2:
                row_str += f"{str(val):<6}"
            else:
                row_str += f"{str(val):<6}"
        print(row_str)