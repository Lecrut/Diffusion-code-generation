def determine_greater_than(x, y):
    truth_map = {True: 1, False: 0}
    result = x > y
    numeric_val = truth_map[result]
    return numeric_val == 1

if __name__ == '__main__':
    sample_x = 42
    sample_y = 17
    outcome = determine_greater_than(sample_x, sample_y)
    print(outcome)