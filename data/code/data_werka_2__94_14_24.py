def contains_truth(values):
    truth_map = {True: 1, False: 0}
    accumulated = 0
    for item in values:
        accumulated += truth_map.get(item, 0)
        if accumulated > 0:
            return True
    return False

if __name__ == '__main__':
    sample_values = [False, False, False, False]
    outcome = contains_truth(sample_values)
    print(outcome)