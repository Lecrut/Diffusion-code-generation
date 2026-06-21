def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]
    for item in lst[1:]:
        if item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min(sample_list))