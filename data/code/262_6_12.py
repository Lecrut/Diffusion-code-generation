def find_min_max(list1, list2):
    min_val = float('inf')
    max_val = float('-inf')

    for num in list1:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    for num in list2:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

if __name__ == '__main__':
    sample_list1 = [3.14, 1.618, 2.718, 0.577]
    sample_list2 = [9.999, -10.5, 42.0, -5.3, 100.1, -100.2]
    min_val, max_val = find_min_max(sample_list1, sample_list2)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")