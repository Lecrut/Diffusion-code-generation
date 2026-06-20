def truth_table_or():
    inputs = [True, False]
    return [{'A': A, 'B': B, 'A or B': A or B} for A in inputs for B in inputs]

if __name__ == '__main__':
    print(truth_table_or())