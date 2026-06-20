def generate_truth_table():
    variables = ['A', 'B', 'C', 'D']
    truth_values = [0, 1]
    
    for a in truth_values:
        for b in truth_values:
            for c in truth_values:
                for d in truth_values:
                    print(f"{variables[0]}: {a}, {variables[1]}: {b}, {variables[2]}: {c}, {variables[3]}: {d}")

if __name__ == '__main__':
    generate_truth_table()