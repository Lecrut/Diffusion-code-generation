CONDITIONS = ['P', 'Q']
NUM_CONDITIONS = len(CONDITIONS)
NUM_ROWS = 2 ** NUM_CONDITIONS

def print_truth_table():
    print("Truth Table for P, Q")
    for i in range(NUM_ROWS):
        row_values = []
        for j in range(NUM_CONDITIONS):
            if (i >> j) & 1:
                row_values.append('1')
            else:
                row_values.append('0')
        print(" ".join(row_values))

if __name__ == '__main__':
    print_truth_table()