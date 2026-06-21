def count_target_value(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
    target_value = 2
    if isinstance(sample_list, list) and isinstance(target_value, int):
        print(count_target_value(sample_list, target_value))
    else:
        raise ValueError("Invalid input: sample_list must be a list and target_value must be an integer")