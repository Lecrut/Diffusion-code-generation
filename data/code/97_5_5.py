def generate_truth_table():
    conditions = ['A', 'B', 'C', 'D']
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                for d in [True, False]:
                    print(f"{conditions[0]}: {a}, {conditions[1]}: {b}, {conditions[2]}: {c}, {conditions[3]}: {d}")

if __name__ == '__main__':
    generate_truth_table()