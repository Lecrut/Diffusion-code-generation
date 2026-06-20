def generate_truth_table():
    table = []
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                for d in [0, 1]:
                    table.append((a, b, c, d))
    return table

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(f"A: {row[0]}, B: {row[1]}, C: {row[2]}, D: {row[3]}")