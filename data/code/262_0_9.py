def find_min_max(lst):
    if not lst:
        return None, None
    min_val = max_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, -2, 7]
    print(find_min_max(sample_list))