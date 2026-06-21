def implication_table():
    truth_values = [True, False]
    table = [[A, B, (not A) or B] for A in truth_values for B in truth_values]
    return table

if __name__ == '__main__':
    result = implication_table()
    print(result)