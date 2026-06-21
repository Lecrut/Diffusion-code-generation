def generate_truth_table():
    truth_table = []
    for p in range(2):
        for q in range(2):
            for r in range(2):
                row = [p, q, r]
                truth_table.append(row)
    return truth_table

if __name__ == '__main__':
    result = generate_truth_table()
    print(result)