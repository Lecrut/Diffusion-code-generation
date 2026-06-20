def generate_truth_table():
    operations = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NOT': lambda x: not x,
        'XOR': lambda x, y: x != y,
        'NAND': lambda x, y: not (x and y),
        'NOR': lambda x, y: not (x or y),
        'IMPLIES': lambda x, y: not x or y
    }

    results = {}
    for a in [True, False]:
        for b in [True, False]:
            row = {key: operations[key](a, b) for key in operations}
            results[(a, b)] = row

    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)