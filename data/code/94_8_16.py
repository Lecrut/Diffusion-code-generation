def check_truth_presence(input_list):
    if not isinstance(input_list, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(input_list) == 0:
        return False
    for element in input_list:
        if element is True:
            return True
    return False

if __name__ == '__main__':
    test_values = [False, False, True, False]
    result = check_truth_presence(test_values)
    print(result)