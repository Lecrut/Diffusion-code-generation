def find_minimum(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [10, -5, 3, 0, 7, -20, 4]
    result = find_minimum(sample_list)
    print(result)