def generate_truth_table(n):
    num_rows = 2**n
    truth_table = []
    for i in range(num_rows):
        binary_representation = format(i, f'0{n}b')
        row = [int(bit) for bit in binary_representation]
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    N = 3
    truth_table_data = generate_truth_table(N)
    for row in truth_table_data:
        print(row)