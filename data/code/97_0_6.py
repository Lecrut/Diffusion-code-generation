def print_truth_table():
    for a in [True, False]:
        for b in [True, False]:
            print(f"A: {a}, B: {b}, A AND B: {a and b}, A OR B: {a or b}, NOT A: {not a}, NOT B: {not b}")

if __name__ == '__main__':
    print_truth_table()