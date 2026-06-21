def generate_truth_table():
    combinations = list(itertools.product([0, 1], repeat=2))
    truth_table = []
    for a, b in combinations:
        row = [a, b, int(a == 0 or b)]
        truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    truth_table_result = generate_truth_table()
    for row in truth_table_result:
        print(row)