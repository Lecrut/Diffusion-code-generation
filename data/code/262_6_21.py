def find_min_max(list1, list2):
    if not (list1 and list2):
        raise ValueError("Both lists must contain at least one element")

    min_val = max_val = None

    for num in list1 + list2:
        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num

    return min_val, max_val

if __name__ == '__main__':
    sample_list1 = [3.14, 1.618, 2.718, 0.577]
    sample_list2 = [9.999, -10.5, 42.0, -5.3]
    min_val, max_val = find_min_max(sample_list1, sample_list2)
    print("Minimum value:", min_val)
    print("Maximum value:", max_val)