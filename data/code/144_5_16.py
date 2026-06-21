def generate_truth_table():
    truth_table = []
    for p in range(2):
        for q in range(2):
            for r in range(2):
                truth_table.append((p, q, r))
    return truth_table

if __name__ == '__main__':
    table = generate_truth_table()
    print(table)