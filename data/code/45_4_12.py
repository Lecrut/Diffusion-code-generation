def find_minimum(lst):
    if not lst:
        raise ValueError("List is empty")
    min_val = lst[0]
    for val in lst[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 7, 2, 8, 4, 6, 0]
    result = find_minimum(sample_values)
    print(result)