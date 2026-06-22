def has_true_value(values):
    truth_map = {True: 1, False: 0}
    total = sum(truth_map.get(v, 0) for v in values)
    return total > 0

if __name__ == '__main__':
    sample_data = [False, False, False, False]
    outcome = has_true_value(sample_data)
    print(outcome)