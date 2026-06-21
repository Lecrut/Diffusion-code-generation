if __name__ == '__main__':
    truth_table = [[A, B, A <= B] for A in [False, True] for B in [False, True]]
    print(truth_table)