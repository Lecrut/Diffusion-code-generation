def validate_truth_table():
    P_values = [0, 1]
    Q_values = [0, 1]
    for p in P_values:
        for q in Q_values:
            if (p and q) or (not p and not q):
                continue
            return False
    return True

if __name__ == '__main__':
    result = validate_truth_table()
    print(result)