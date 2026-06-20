def generate_truth_table():
    inputs = [True, False]
    for a in inputs:
        for b in inputs:
            print(f"{a} AND {b} = {a and b}")

if __name__ == '__main__':
    generate_truth_table()