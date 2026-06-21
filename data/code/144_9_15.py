def generate_truth_table(n):
    num_rows = 2**n
    truth_table = [[(i >> j) & 1 for j in range(n)] + [((i >> j) & 1) == ((i >> (j+1)) & 1) for j in range(n-1)] for i in range(num_rows)]
    return truth_table

if __name__ == '__main__':
    N = 3
    truth_table_data = generate_truth_table(N)
    for row in truth_table_data:
        print(" ".join(str(bit) for bit in row))