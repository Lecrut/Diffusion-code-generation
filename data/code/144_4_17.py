def generate_truth_table():
    truth_table = []
    for A in range(2):
        for B in range(2):
            result = "T" if (A == 0 or B == 1) else "F"
            truth_table.append((A, B, result))
    return truth_table

if __name__ == '__main__':
    table = generate_truth_table()
    for row in table:
        print(row)