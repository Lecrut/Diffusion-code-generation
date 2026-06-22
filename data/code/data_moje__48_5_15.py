def find_largest_value(*lists):
    largest = None
    for lst in lists:
        for val in lst:
            if largest is None or val > largest:
                largest = val
    return largest

if __name__ == '__main__':
    list1 = [1, 5, 3]
    list2 = [9, 2, 6]
    list3 = [4, 8, 7]
    result = find_largest_value(list1, list2, list3)
    print(result)