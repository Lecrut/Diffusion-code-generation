def generate_truth_table():
    return [[A, B, A == B] for A in [False, True] for B in [False, True]]

if __name__ == '__main__':
    print(generate_truth_table())