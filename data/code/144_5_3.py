def generate_truth_table():
    for p in range(2):
        for q in range(2):
            for r in range(2):
                print(f"P={p}, Q={q}, R={r}")

if __name__ == '__main__':
    generate_truth_table()