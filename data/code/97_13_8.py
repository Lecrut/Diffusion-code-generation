BOOL_VALUES = [True, False]

def generate_and_truth_table():
    for a in BOOL_VALUES:
        for b in BOOL_VALUES:
            print(f"{a} AND {b} = {a and b}")

if __name__ == '__main__':
    generate_and_truth_table()