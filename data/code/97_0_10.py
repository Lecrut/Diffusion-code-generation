def print_truth_table():
    for p in [True, False]:
        for q in [True, False]:
            print(f"{p} AND {q}: {p and q}")

if __name__ == '__main__':
    print_truth_table()