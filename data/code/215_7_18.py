def flatten_and_find_max(nested_list):
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(flatten_and_find_max(sublist))
        else:
            flat_list.append(sublist)
    return max(flat_list)

if __name__ == '__main__':
    nested_list1 = [[1, 5], [3, 2], [9, 4]]
    nested_list2 = [[[1]], [2], [3, [4]]]
    print(f"Max in {nested_list1}: {flatten_and_find_max(nested_list1)}")
    print(f"Max in {nested_list2}: {flatten_and_find_max(nested_list2)}")