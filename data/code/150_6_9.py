def exclude_target_from_list(input_list, target_value):
    return [item for item in input_list if item != target_value]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    target_value = 2
    result = exclude_target_from_list(sample_list, target_value)
    print(result)