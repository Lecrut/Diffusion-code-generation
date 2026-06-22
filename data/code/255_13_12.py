def find_maximum(data):
    if isinstance(data, list):
        return max(map(find_maximum, data))
    return data

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1]
    nested_list = [list1, list2, [10, 20, 30]]
    empty_list = []
    single_element = [42.0]

    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {nested_list}: {find_maximum(nested_list)}")
    print(f"Maximum of {empty_list}: None")
    print(f"Maximum of {single_element}: {find_maximum(single_element)}")