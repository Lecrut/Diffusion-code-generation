NUM_VARIABLES = 3

def generate_truth_table():
    num_rows = 2 ** NUM_VARIABLES
    truth_table = []
    for i in range(num_rows):
        row = []
        for j in range(NUM_VARIABLES):
            if (i >> j) & 1:
                row.append(True)
            else:
                row.append(False)
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    sample_result = generate_truth_table()
    print(sample_result)