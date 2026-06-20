def generate_truth_table(vars):
    table = []
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                for d in [0, 1]:
                    table.append((a, b, c, d))
    return table

if __name__ == '__main__':
    truth_table = generate_truth_table(['A', 'B', 'C', 'D'])
    for row in truth_table:
        print(f"{row[0]}: {row[1]}, {row[2]}: {row[3]}")