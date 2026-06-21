def remove_target(lst, target):
    return [x for x in lst if x != target]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    target_value = 3
    result = remove_target(sample_list, target_value)
    print(result)