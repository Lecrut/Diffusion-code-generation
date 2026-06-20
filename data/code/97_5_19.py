def generate_truth_table():
    conditions = ['A', 'B', 'C', 'D']
    truth_values = [True, False]
    
    for a in truth_values:
        for b in truth_values:
            for c in truth_values:
                for d in truth_values:
                    print(f"{a} {b} {c} {d}")

if __name__ == '__main__':
    generate_truth_table()