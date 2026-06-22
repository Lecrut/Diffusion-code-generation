def find_minimum_with_early_exit(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [42, -7, 15, 3, 88, -23, 5, 0]
    result = find_minimum_with_early_exit(sample_list)
    print(result)