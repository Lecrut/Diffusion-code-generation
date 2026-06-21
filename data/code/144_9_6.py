def generate_truth_table():
    return [[A == B for B in [False, True]] for A in [False, True]]

if __name__ == '__main__':
    print(generate_truth_table())