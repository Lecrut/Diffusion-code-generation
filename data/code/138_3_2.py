def generate_or_truth_table(bool_list):
    n = len(bool_list)
    rows = 2**n
    truth_table = []
    for i in range(rows):
        row = []
        for j in range(n):
            if (i >> j) & 1:
                row.append(bool_list[j])
            else:
                row.append(not bool_list[j])
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    sample_inputs = [False, True]
    truth_table_result = generate_or_truth_table(sample_inputs)
    for row in truth_table_result:
        print(row)