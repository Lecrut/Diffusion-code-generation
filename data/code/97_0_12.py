def print_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"{a} AND {b} = {a and b}")
            print(f"{a} OR {b} = {a or b}")
            print(f"NOT {a} = {not a}")
            print(f"NOT {b} = {not b}")

if __name__ == '__main__':
    print_truth_table()