def find_min(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for val in lst:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min(sample_list))