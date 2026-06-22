def check_truth_presence(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if len(input_list) == 0:
        return False
    for element in input_list:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    test_data = [False, False, True, False]
    result = check_truth_presence(test_data)
    print(result)