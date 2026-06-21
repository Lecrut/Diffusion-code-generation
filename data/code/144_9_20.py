def generate_truth_table():
    return [[A == B for B in [True, False]] for A in [True, False]]

if __name__ == '__main__':
    print(generate_truth_table())