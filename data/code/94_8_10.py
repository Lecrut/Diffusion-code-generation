def check_truth_presence(boolean_list):
    if not boolean_list:
        return False
    for element in boolean_list:
        if element:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, True, False]
    found = check_truth_presence(test_data)
    print(found)