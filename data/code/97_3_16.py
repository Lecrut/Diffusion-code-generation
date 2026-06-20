def print_truth_table():
    P = [0, 1]
    Q = [0, 1]
    
    print("P | Q | P -> Q")
    for p in P:
        for q in Q:
            result = int(not p or q)
            print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    print_truth_table()