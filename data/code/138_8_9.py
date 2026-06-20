P_VALUES = [0, 1]
Q_VALUES = [0, 1]

def check_truth_table():
    results = []
    for p in P_VALUES:
        for q in Q_VALUES:
            result = (p and q) or (not p and not q)
            results.append((p, q, result))
    return results

if __name__ == '__main__':
    truth_table_results = check_truth_table()
    print("P | Q | Result")
    print("-" * 15)
    for p, q, result in truth_table_results:
        print(f"{p} | {q} | {result}")