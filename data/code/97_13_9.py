def generate_and_truth_table():
    inputs = [True, False]
    for a in inputs:
        for b in inputs:
            result = a and b
            print(f"{a} AND {b} = {result}")

if __name__ == '__main__':
    generate_and_truth_table()