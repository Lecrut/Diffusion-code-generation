def compare_list_sizes(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    if size1 > size2:
        return list1, "List 1 is larger"
    elif size2 > size1:
        return list2, "List 2 is larger"
    else:
        return None, "Lists are the same size"
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30]
    result_list, result_message = compare_list_sizes(list_a, list_b)
    if result_list is not None:
        print(f"{result_list} is larger")
    else:
        print("Lists are the same size")