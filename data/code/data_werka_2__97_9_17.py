def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    headers = ["A", "B", "A AND B", "A OR B", "A XOR B", "NOT A", "NOT B"]
    separator = "-" * 45
    print(separator)
    print(f"{headers[0]:<5} {headers[1]:<5} {headers[2]:<9} {headers[3]:<9} {headers[4]:<9} {headers[5]:<7} {headers[6]:<7}")
    print(separator)
    
    table = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            and_res = val_a and val_b
            or_res = val_a or val_b
            xor_res = val_a != val_b
            not_a = not val_a
            not_b = not val_b
            
            row = (val_a, val_b, and_res, or_res, xor_res, not_a, not_b)
            table.append(row)
            
            print(f"{str(val_a):<5} {str(val_b):<5} {str(and_res):<9} {str(or_res):<9} {str(xor_res):<9} {str(not_a):<7} {str(not_b):<7}")
            
    print(separator)
    return table

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = generate_truth_table(sample_a, sample_b)
    print(result)