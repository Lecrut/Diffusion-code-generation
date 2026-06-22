def contains_true(values):
    truth_map = {True: 1, False: 0}
    accumulator = 0
    for item in values:
        accumulator += truth_map.get(item, 0)
        if accumulator > 0:
            return True
    return False

if __name__ == '__main__':
    test_values = [False, False, False, False]
    outcome = contains_true(test_values)
    print(outcome)