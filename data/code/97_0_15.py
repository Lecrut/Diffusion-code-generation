def generate_truth_table():
    P_values = [True, False]
    Q_values = [True, False]
    print("P | Q | P AND Q")
    print("---|---|---------")
    for p in P_values:
        for q in Q_values:
            p_and_q = p and q
            print(f"{p} | {q} | {p_and_q}")

if __name__ == '__main__':
    generate_truth_table()