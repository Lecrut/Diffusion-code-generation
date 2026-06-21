NUM_VARS = 3

def generate_truth_table(n):
    num_rows = 2 ** n
    header = ["V" + str(i+1) for i in range(n)]
    truth_table = []
    
    for i in range(num_rows):
        row_values = []
        for j in range(n):
            if (i >> j) & 1:
                row_values.append("T")
            else:
                row_values.append("F")
        truth_table.append(dict(zip(header, row_values)))
    
    return truth_table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table(NUM_VARS)
    for row in sample_truth_table:
        print(row)