def generate_truth_table(n):
    if n == 0:
        return [{'V1': False}]
    truth_table = []
    for i in range(2**n):
        row = {}
        for j in range(n):
            row[f'V{j+1}'] = (i >> j) & 1
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    sample_values = 3
    print(generate_truth_table(sample_values))