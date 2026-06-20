def print_truth_table():
    for a in [False, True]:
        for b in [False, True]:
            result = not a or b
            print(f"{a} -> {b}: {result}")

if __name__ == '__main__':
    print_truth_table()