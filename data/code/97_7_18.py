def generate_truth_table(variables):
    if not variables:
        raise ValueError("At least one boolean variable is required")
    
    num_variables = len(variables)
    header = " | ".join(variables) + " | AND | OR | XOR\n"
    separator = "-" * (len(header) - 1) + "\n"
    
    print(separator)
    print(header)
    print(separator)
    
    for i in range(2 ** num_variables):
        row_values = []
        for j in range(num_variables):
            row_values.append("T" if i & (1 << j) else "F")
        
        and_result = "T" if all(row_values[:num_variables]) else "F"
        or_result = "T" if any(row_values[:num_variables]) else "F"
        xor_result = "T" if row_values.count("T") == 1 else "F"
        
        print(" | ".join(row_values) + f" | {and_result} | {or_result} | {xor_result}")
    
    print(separator)

if __name__ == '__main__':
    sample_variables = ["P", "Q", "R"]
    generate_truth_table(sample_variables)