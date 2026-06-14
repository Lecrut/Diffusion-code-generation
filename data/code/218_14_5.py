def find_minimum_in_list_of_lists(list_of_lists):
    if not list_of_lists:
        raise ValueError("Input list of lists is empty")
    minimum = None
    is_first = True
    for sublist in list_of_lists:
        if not sublist:
            continue
        current_min = sublist[0]
        if is_first:
            minimum = current_min
            is_first = False
        else:
            if current_min < minimum:
                minimum = current_min
    if minimum is None:
        raise ValueError("All sublists were empty")
    return minimum
if __name__ == '__main__':
    list1 = [[1, 5, 3], [8, 2, 9], [4, 7]]
    list2 = [[10, 20], [5, 15]]
    list3 = []
    list4 = [[]]
    list5 = [[-5], [], [100]]
    print(f"List 1: {list1}, Minimum: {find_minimum_in_list_of_lists(list1)}")
    print(f"List 2: {list2}, Minimum: {find_minimum_in_list_of_lists(list2)}")
    print(f"List 3: {list3}")
    try:
        find_minimum_in_list_of_lists(list3)
    except ValueError as e:
        print(f"Error for List 3: {e}")
    try:
        result4 = find_minimum_in_list_of_lists(list4)
        print(f"List 4: {list4}, Minimum: {result4}")
    except ValueError as e:
        print(f"Error for List 4: {e}")
    try:
        result5 = find_minimum_in_list_of_lists(list5)
        print(f"List 5: {list5}, Minimum: {result5}")
    except ValueError as e:
        print(f"Error for List 5: {e}")