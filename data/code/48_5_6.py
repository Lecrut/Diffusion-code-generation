def find_largest_across_lists(*lists):
    if not lists:
        raise ValueError("No lists provided")
    largest = None
    for lst in lists:
        for item in lst:
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    list1 = [1, 5, 3]
    list2 = [9, 2, 7]
    list3 = [4, 8, 6]
    result = find_largest_across_lists(list1, list2, list3)
    print(result)