def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            and_res = val_a and val_b
            or_res = val_a or val_b
            xor_res = val_a != val_b
            nand_res = not (val_a and val_b)
            nor_res = not (val_a or val_b)
            implies_res = (not val_a) or val_b
            
            results.append({
                'A': val_a,
                'B': val_b,
                'A AND B': and_res,
                'A OR B': or_res,
                'A XOR B': xor_res,
                'A NAND B': nand_res,
                'A NOR B': nor_res,
                'A IMPLIES B': implies_res
            })
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    table = generate_truth_table(sample_a, sample_b)
    headers = list(table[0].keys())
    col_widths = [max(len(str(h)), max(len(str(row[h])) for row in table)) + 2 for h in headers]
    
    header_line = "".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-" * sum(col_widths))
    
    for row in table:
        line = "".join(str(row[h]).ljust(col_widths[i]) for i, h in enumerate(headers))
        print(line)
    
    print(table)