def generate_truth_table():
    conditions = ['A', 'B', 'C', 'D']
    truth_values = [False, True]

    for a in truth_values:
        for b in truth_values:
            for c in truth_values:
                for d in truth_values:
                    print(f"{conditions[0]}: {a}, {conditions[1]}: {b}, {conditions[2]}: {c}, {conditions[3]}: {d}")

if __name__ == '__main__':
    generate_truth_table()