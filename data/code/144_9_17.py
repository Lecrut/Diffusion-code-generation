def generate_truth_table(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    num_rows = 2**n
    truth_table = [[(i >> j) & 1 for j in range(n)] for i in range(num_rows)]
    return truth_table

if __name__ == '__main__':
    n_vars = 3
    try:
        truth_table_data = generate_truth_table(n_vars)
        for row in truth_table_data:
            print(" ".join(map(str, row)))
    except ValueError as e:
        print(e)