def find_minimum(lst):
    if not lst:
        return None
    min_val = lst[0]
    for item in lst[1:]:
        if item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_list = [3, -1, 7, 0, 15, -8, 4]
    result = find_minimum(sample_list)
    print(result)