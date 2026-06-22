def find_largest_across_lists(lists):
    largest = None
    for lst in lists:
        for item in lst:
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [-1, -2, -3]
    result = find_largest_across_lists([list1, list2, list3])
    print(result)