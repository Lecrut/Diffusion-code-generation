P_VALUES = [0, 1]
Q_VALUES = [0, 1]

def validate_truth_table():
    print("A | B | (A and B) OR (not A and not B)")
    print("-" * 40)
    for a in P_VALUES:
        for b in Q_VALUES:
            result = (a and b) or (not a and not b)
            print(f"{a} | {b} | {result}")

if __name__ == '__main__':
    validate_truth_table()