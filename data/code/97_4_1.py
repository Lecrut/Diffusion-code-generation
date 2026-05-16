def generate_truth_table():
    P_values = [False, True]
    Q_values = [False, True]
    print("P | Q | P -> Q")
    for p in P_values:
        for q in Q_values:
            result = not p or q
            print(f"{p} | {q} | {result}")
if __name__ == '__main__':
    generate_truth_table()