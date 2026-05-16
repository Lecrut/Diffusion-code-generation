def generate_truth_table():
    P_values = [0, 1]
    Q_values = [0, 1]
    print("P | Q | P AND Q")
    print("---|---|---------")
    for p in P_values:
        for q in Q_values:
            p_and_q = p & q
            print(f"{p} | {q} | {p_and_q}")
if __name__ == '__main__':
    generate_truth_table()