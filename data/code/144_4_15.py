def generate_truth_table():
    truth_table = []
    for A in [True, False]:
        for B in [True, False]:
            implication_result = not A or B
            truth_table.append((A, B, implication_result))
    return truth_table

if __name__ == '__main__':
    truth_table_result = generate_truth_table()
    for row in truth_table_result:
        print(row)