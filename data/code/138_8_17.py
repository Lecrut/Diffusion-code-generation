P_VALUES = [0, 1]
Q_VALUES = [0, 1]

def validate_truth_table():
    results = []
    for p in P_VALUES:
        for q in Q_VALUES:
            result = (p and q) or (not p and not q)
            results.append(result)
    return all(results)

if __name__ == '__main__':
    print(validate_truth_table())