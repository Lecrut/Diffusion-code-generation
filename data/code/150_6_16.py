def exclude_target(lst, target):
    return [x for x in lst if x != target]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    target_value = 2
    result = exclude_target(sample_list, target_value)
    print(result)