def exclude_target(lst, target):
    return [item for item in lst if item != target]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    target_value = 3
    result = exclude_target(sample_list, target_value)
    print(result)