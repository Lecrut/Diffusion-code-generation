def generate_truth_table():
    return [[A, B, A == B] for A in [True, False] for B in [True, False]]

if __name__ == '__main__':
    print(generate_truth_table())