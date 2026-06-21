def check_boolean_uniformity(values):
    if not values:
        return True
    truth_count = 0
    false_count = 0
    for item in values:
        if item:
            truth_count += 1
        else:
            false_count += 1
    return truth_count == 0 or false_count == 0

if __name__ == '__main__':
    test_data = [False, False, False]
    outcome = check_boolean_uniformity(test_data)
    print(outcome)