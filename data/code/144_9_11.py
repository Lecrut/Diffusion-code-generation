def validate_input(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

def generate_truth_table(n):
    validate_input(n)
    num_rows = 2**n
    truth_table = [[(i >> j) & 1 for j in range(n)] for i in range(num_rows)]
    return truth_table

if __name__ == '__main__':
    N = 3
    truth_table_data = generate_truth_table(N)
    for row in truth_table_data:
        print(" ".join(str(bit) for bit in row))