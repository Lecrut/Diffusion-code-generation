def generate_truth_table(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Number of variables must be a positive integer")
    
    num_rows = 2**n
    truth_table = [[(i >> j) & 1 for j in range(n)] for i in range(num_rows)]
    return truth_table

if __name__ == '__main__':
    n_vars = 3
    truth_table_data = generate_truth_table(n_vars)
    for row in truth_table_data:
        print(row)