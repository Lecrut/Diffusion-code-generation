def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]
    for val in lst[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1, 9]
    print(find_min(sample_list))