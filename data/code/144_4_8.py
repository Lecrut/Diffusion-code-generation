def generate_truth_table():
    truth_table = []
    for A in [False, True]:
        for B in [False, True]:
            implication_result = not A or B
            truth_table.append((A, B, implication_result))
    return truth_table

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)