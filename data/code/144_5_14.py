TRUTH_TABLE_SIZE = 8

def generate_truth_table():
    truth_table = []
    for i in range(TRUTH_TABLE_SIZE):
        row = [(i >> j) & 1 for j in range(3)]
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    sample_result = generate_truth_table()
    print(sample_result)