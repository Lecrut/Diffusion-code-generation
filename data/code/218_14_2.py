def find_minimum_in_list_of_lists(list_of_lists):
    if not list_of_lists:
        raise ValueError("Input list of lists is empty")
    min_value = None
    is_first = True
    for sublist in list_of_lists:
        if not sublist:
            continue
        current_min = sublist[0]
        if is_first:
            min_value = current_min
            is_first = False
        else:
            if current_min < min_value:
                min_value = current_min
    return min_value
if __name__ == '__main__':
    list1 = [[1, 5, 3], [8, 2, 9], [4, 6]]
    list2 = [[10, 20], [30, 40]]
    list3 = []
    list4 = [[]]
    list5 = [[-5], [100], [-10]]
    print(f"List 1: {list1}, Minimum: {find_minimum_in_list_of_lists(list1)}")
    print(f"List 2: {list2}, Minimum: {find_minimum_in_list_of_lists(list2)}")
    print(f"List 3: {list3}")
    try:
        find_minimum_in_list_of_lists(list3)
    except ValueError as e:
        print(f"Error for List 3: {e}")
    print(f"List 4: {list4}, Minimum: {find_minimum_in_list_of_lists(list4)}")
    print(f"List 5: {list5}, Minimum: {find_minimum_in_list_of_lists(list5)}")