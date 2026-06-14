def find_minimum_in_list_of_lists(list_of_lists):
    if not list_of_lists:
        raise ValueError("Input list of lists is empty")
    min_element = None
    for sublist in list_of_lists:
        if not sublist:
            continue
        current_min = min(sublist)
        if min_element is None:
            min_element = current_min
        else:
            if current_min < min_element:
                min_element = current_min
    if min_element is None:
        raise ValueError("All sublists were empty")
    return min_element
if __name__ == '__main__':
    list1 = [[1, 5, 3], [8, 2, 9], [4, 7]]
    list2 = [[10, 20], [5, 15]]
    list3 = []
    list4 = [[-5], [], [100]]
    list5 = [[], [], []]
    print(f"Result for {list1}: {find_minimum_in_list_of_lists(list1)}")
    print(f"Result for {list2}: {find_minimum_in_list_of_lists(list2)}")
    try:
        result4 = find_minimum_in_list_of_lists(list4)
        print(f"Result for {list4}: {result4}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")
    try:
        result5 = find_minimum_in_list_of_lists(list5)
        print(f"Result for {list5}: {result5}")
    except ValueError as e:
        print(f"Error for {list5}: {e}")
    try:
        find_minimum_in_list_of_lists(list3)
    except ValueError as e:
        print(f"Error for {list3}: {e}")