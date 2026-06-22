def find_largest_across_lists(*lists):
    if not lists:
        return None
    max_value = None
    for lst in lists:
        for item in lst:
            if max_value is None or item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15, 25, 35, 45]
    list3 = [100, 200, 50]
    result = find_largest_across_lists(list1, list2, list3)
    print(result)