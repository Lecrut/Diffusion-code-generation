def generate_truth_table(n):
    truth_table = []
    for i in range(2**n):
        row = {}
        for j in range(n):
            row[j] = (i >> j) & 1
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table(3)
    print(sample_truth_table)