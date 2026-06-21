def generate_truth_table(a: bool, b: bool) -> list:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    
    combinations = [(True, True), (True, False), (False, True), (False, False)]
    table = []
    
    for val_a, val_b in combinations:
        and_res = val_a and val_b
        or_res = val_a or val_b
        xor_res = val_a != val_b
        not_a = not val_a
        not_b = not val_b
        
        table.append({
            "A": val_a,
            "B": val_b,
            "A AND B": and_res,
            "A OR B": or_res,
            "A XOR B": xor_res,
            "NOT A": not_a,
            "NOT B": not_b
        })
        
    return table

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = generate_truth_table(sample_a, sample_b)
    
    header = "{:<5} {:<5} {:<9} {:<9} {:<9} {:<7} {:<7}"
    separator = "-" * 55
    
    print(separator)
    print(header.format("A", "B", "A AND B", "A OR B", "A XOR B", "NOT A", "NOT B"))
    print(separator)
    
    for row in result:
        print(header.format(
            str(row["A"]),
            str(row["B"]),
            str(row["A AND B"]),
            str(row["A OR B"]),
            str(row["A XOR B"]),
            str(row["NOT A"]),
            str(row["NOT B"])
        ))
    
    print(separator)
    
    computed_values = [
        (row["A"], row["B"], row["A AND B"]) 
        for row in result
    ]
    print(computed_values)