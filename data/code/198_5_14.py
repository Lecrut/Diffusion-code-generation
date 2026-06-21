def min_value(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(min_value(sample_list))