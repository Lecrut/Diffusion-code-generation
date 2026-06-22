def find_largest_value(*lists):
    if not lists:
        raise ValueError("At least one list must be provided")
    
    largest = None
    for lst in lists:
        if not lst:
            continue
        for val in lst:
            if largest is None or val > largest:
                largest = val
    return largest

if __name__ == '__main__':
    list1 = [10, 25, 3, 8]
    list2 = [100, 4, 15, 22]
    list3 = [7, 45, 60, 1]
    result = find_largest_value(list1, list2, list3)
    print(result)