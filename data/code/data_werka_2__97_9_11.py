def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    headers = ("A", "B", "A AND B", "A OR B", "A XOR B", "NOT A", "NOT B")
    rows = []
    
    for val_a in [True, False]:
        for val_b in [True, False]:
            and_val = val_a and val_b
            or_val = val_a or val_b
            xor_val = val_a != val_b
            not_a = not val_a
            not_b = not val_b
            rows.append((val_a, val_b, and_val, or_val, xor_val, not_a, not_b))
            
    sep = "-" * 50
    print(sep)
    print(f"{headers[0]:<5} {headers[1]:<5} {headers[2]:<9} {headers[3]:<9} {headers[4]:<9} {headers[5]:<7} {headers[6]:<7}")
    print(sep)
    
    for row in rows:
        print(f"{str(row[0]):<5} {str(row[1]):<5} {str(row[2]):<9} {str(row[3]):<9} {str(row[4]):<9} {str(row[5]):<7} {str(row[6]):<7}")
        
    return rows

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = generate_truth_table(sample_a, sample_b)
    print(result)