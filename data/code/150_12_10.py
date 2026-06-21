def validate_target(target, lst):
    if isinstance(target, int) and 0 <= target < len(lst):
        return True, "index"
    elif target in lst:
        return True, "value"
    else:
        raise ValueError('Target not found in list')

def remove_item(lst, target):
    is_valid, target_type = validate_target(target, lst)
    if target_type == "index":
        return lst[:target] + lst[target + 1:]
    elif target_type == "value":
        return [item for item in lst if item != target]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(remove_item(sample_list, 2))
    print(remove_item(sample_list, 3))
    try:
        print(remove_item(sample_list, 6))
    except ValueError as e:
        print(e)