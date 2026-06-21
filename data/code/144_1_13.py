def generate_truth_table(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    num_rows = 2 ** n
    header = {f"V{i+1}": False for i in range(n)}
    truth_table = [header.copy() for _ in range(num_rows)]
    
    for i in range(num_rows):
        for j in range(n):
            truth_table[i][f"V{j+1}"] = (i >> j) & 1
    
    return truth_table

if __name__ == '__main__':
    sample_n = 3
    table = generate_truth_table(sample_n)
    print(table)