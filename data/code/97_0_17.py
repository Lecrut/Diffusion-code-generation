def print_truth_table():
    for p in [True, False]:
        for q in [True, False]:
            print(f"p: {p}, q: {q}, p or q: {p or q}, not p: {not p}")

if __name__ == '__main__':
    print_truth_table()