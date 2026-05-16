def compare_list_sizes(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    if size1 > size2:
        return list1, "List 1 is larger"
    elif size2 > size1:
        return list2, "List 2 is larger"
    else:
        return list1, "Lists are the same size"
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30]
    larger_list, message = compare_list_sizes(list_a, list_b)
    print(f"List A: {list_a}, Size: {len(list_a)}")
    print(f"List B: {list_b}, Size: {len(list_b)}")
    print(f"Result: {larger_list} is larger")