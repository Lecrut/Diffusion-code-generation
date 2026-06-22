def is_largest_greater_than_target(lst, target):
    if not lst:
        return False
    if len(lst) == 1:
        return lst[0] > target
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    return (is_largest_greater_than_target(left_half, target) or 
            is_largest_greater_than_target(right_half, target))

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 7, 2]
    target_value = 6
    result = is_largest_greater_than_target(sample_list, target_value)
    print(result)