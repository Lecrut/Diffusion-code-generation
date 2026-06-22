def is_largest_greater_than_target(lst, target):
    if not lst:
        return False
    largest = max(lst)
    return largest > target

if __name__ == '__main__':
    sample_list = [3, 5, 7, 2]
    target_value = 4
    result = is_largest_greater_than_target(sample_list, target_value)
    print(result)