def is_largest_greater_than_target(lst, target):
    if not lst:
        return False
    if len(lst) == 1:
        return lst[0] > target
    mid = len(lst) // 2
    left_max = max(lst[:mid])
    right_max = max(lst[mid:])
    return (left_max > target or is_largest_greater_than_target(lst[:mid], target)) and \
           (right_max > target or is_largest_greater_than_target(lst[mid:], target))

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target_value = 7
    result = is_largest_greater_than_target(sample_list, target_value)
    print(result)