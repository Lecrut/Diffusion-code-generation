def find_min(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for val in lst[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min(sample_list))