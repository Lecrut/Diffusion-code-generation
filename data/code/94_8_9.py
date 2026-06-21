def check_for_truth(values):
    if not values:
        return False
    for element in values:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, False, False]
    found_truth = check_for_truth(test_data)
    print(found_truth)