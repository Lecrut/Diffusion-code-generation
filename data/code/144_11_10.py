def construct_truth_table():
    truth_values = [True, False]
    implication_table = [[(P, Q, (not P) or Q) for Q in truth_values] for P in truth_values]
    return implication_table

if __name__ == '__main__':
    table = construct_truth_table()
    print(table)