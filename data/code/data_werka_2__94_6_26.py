def has_true_element(values):
    if not values:
        return False
    for item in values:
        if item:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, False, False]
    test_data.append(True)
    test_data.extend([False, False])
    result = has_true_element(test_data)
    print(result)