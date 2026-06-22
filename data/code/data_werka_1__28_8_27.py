def is_largest_greater_than_target(lst, target):
    if not lst:
        return False
    if len(lst) == 1:
        return lst[0] > target
    mid = len(lst) // 2
    left_max = max(lst[:mid])
    right_max = max(lst[mid:])
    largest = max(left_max, right_max)
    return largest > target

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    target_value = 7
    result = is_largest_greater_than_target(sample_list, target_value)
    print(result)