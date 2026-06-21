P = 0
Q = 1
R = 2

TRUTH_TABLE_SIZE = 8

def generate_truth_table():
    truth_table = []
    for i in range(TRUTH_TABLE_SIZE):
        row = [bool(i & (1 << p)) for p in range(3)]
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    sample_result = generate_truth_table()
    print(sample_result)