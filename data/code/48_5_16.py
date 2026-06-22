def find_largest_across_lists(*lists):
    largest = None
    for lst in lists:
        for item in lst:
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = [5, 15, 25]
    list3 = [100, 200, 50]
    result = find_largest_across_lists(list1, list2, list3)
    print(result)