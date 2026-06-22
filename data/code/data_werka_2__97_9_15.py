def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    inputs = [True, False]
    table_rows = []
    
    for val_a in inputs:
        for val_b in inputs:
            logical_and = val_a and val_b
            logical_or = val_a or val_b
            logical_xor = val_a ^ val_b
            logical_not_a = not val_a
            logical_not_b = not val_b
            
            row_data = {
                'A': val_a,
                'B': val_b,
                'A AND B': logical_and,
                'A OR B': logical_or,
                'A XOR B': logical_xor,
                'NOT A': logical_not_a,
                'NOT B': logical_not_b
            }
            table_rows.append(row_data)
            
    return table_rows

if __name__ == '__main__':
    sample_input_a = False
    sample_input_b = True
    truth_table = generate_truth_table(sample_input_a, sample_input_b)
    
    headers = list(truth_table[0].keys())
    print(" | ".join(str(h) for h in headers))
    print("-" * 40)
    
    for row in truth_table:
        row_values = [str(row[h]) for h in headers]
        print(" | ".join(row_values))