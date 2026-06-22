def is_largest_element_greater(lst, target):
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
    sample_list = [3, 5, 7, 2, 8]
    target_value = 6
    result = is_largest_element_greater(sample_list, target_value)
    print(result)