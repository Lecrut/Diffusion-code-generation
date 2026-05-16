if __name__ == '__main__':
    conditions = ['A', 'B', 'C', 'D']
    num_conditions = len(conditions)
    num_rows = 2 ** num_conditions
    print("Truth Table for four input conditions (A, B, C, D):")
    for i in range(num_rows):
        row_values = []
        for j in range(num_conditions):
            if (i >> j) & 1:
                row_values.append('1')
            else:
                row_values.append('0')
        print(" ".join(row_values))