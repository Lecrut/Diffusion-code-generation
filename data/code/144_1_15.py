def generate_truth_table(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    num_vars = n
    num_rows = 2 ** num_vars
    
    header = {f"V{i+1}": False for i in range(num_vars)}
    results = []
    
    def generate(row):
        if len(row) == num_vars:
            results.append({**header, "Result": all(row)})
        else:
            row.append(False)
            generate(row)
            row.pop()
            row.append(True)
            generate(row)
            row.pop()
    
    generate([])
    
    return results

if __name__ == '__main__':
    sample_input = 3
    truth_table = generate_truth_table(sample_input)
    for row in truth_table:
        print(row)