def find_largest_across_lists(lists):
    if not lists:
        raise ValueError('At least one list must be provided')
    largest = float('-inf')
    for lst in lists:
        if lst:
            for item in lst:
                if item > largest:
                    largest = item
    if largest == float('-inf'):
        raise ValueError('All provided lists are empty')
    return largest
if __name__ == '__main__':
    list1 = [1, 5, 3, 9, 2]
    list2 = [15, 7, 3, 12, 8]
    list3 = [-1, -5, 0, 20, 11]
    list4 = [100, 2, 50, 1]
    result = find_largest_across_lists([list1, list2, list3, list4])
    print(result)