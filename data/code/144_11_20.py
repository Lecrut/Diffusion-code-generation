def implication_truth_table():
    truth_table = [
        [False, False, True],
        [False, True, True],
        [True, False, False],
        [True, True, True]
    ]
    return truth_table

if __name__ == '__main__':
    table = implication_truth_table()
    for row in table:
        print(row)