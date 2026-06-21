def remove_target_value(input_list, target):
    if not isinstance(input_list, list) or not all((isinstance(item, (int, float)) for item in input_list)):
        raise ValueError('Input must be a list of numbers')
    if not isinstance(target, (int, float)):
        raise ValueError('Target must be a number')
    return [item for item in input_list if item != target]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(remove_target_value(sample_list, target_value))