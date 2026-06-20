def generate_truth_table(variables):
    num_vars = len(variables)
    header = variables + ['Result']
    print('\t'.join(header))
    
    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars):
            row.append(bool(i & (1 << j)))
        result = all(row[:-1])
        row.append(result)
        print('\t'.join(map(str, row)))

if __name__ == '__main__':
    generate_truth_table(['A', 'B'])