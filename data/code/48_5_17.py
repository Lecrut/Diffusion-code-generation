def find_global_max(*lists):
    largest_value = None
    for lst in lists:
        for item in lst:
            if largest_value is None or item > largest_value:
                largest_value = item
    return largest_value

if __name__ == '__main__':
    list1 = [1, 5, 9]
    list2 = [3, 12, 7]
    list3 = [8, 2, 14]
    result = find_global_max(list1, list2, list3)
    print(result)