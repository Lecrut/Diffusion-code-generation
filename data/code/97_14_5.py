def or_truth_table():
    inputs = [True, False]
    return [{'A': A, 'B': B, 'A OR B': A or B} for A in inputs for B in inputs]

if __name__ == '__main__':
    print(or_truth_table())