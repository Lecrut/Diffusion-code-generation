def exclude_target_from_list(input_list, target_value):
    return [element for element in input_list if element != target_value]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    target = 3
    result = exclude_target_from_list(sample_list, target)
    print(result)