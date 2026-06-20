P_VALUES = [True, False]
Q_VALUES = [True, False]

def print_truth_table_entry(p, q):
    p_and_q = p and q
    print(f"{p} | {q} | {p_and_q}")

if __name__ == '__main__':
    print("P | Q | P AND Q")
    for p in P_VALUES:
        for q in Q_VALUES:
            print_truth_table_entry(p, q)