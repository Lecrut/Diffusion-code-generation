def find_min_max(lst):
    if not lst:
        return None, None
    min_val = max_val = lst[0]
    for value in lst[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_list = [34, 78, 12, 90, 56, 23, 89]
    print(find_min_max(sample_list))