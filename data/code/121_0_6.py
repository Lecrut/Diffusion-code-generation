def compare_list_sizes(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    if size1 > size2:
        return list1, "list1 is larger"
    elif size2 > size1:
        return list2, "list2 is larger"
    else:
        return list1, "lists are the same size"
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30]
    list_c = [5, 6, 7, 8]
    result_ab, message_ab = compare_list_sizes(list_a, list_b)
    print(f"Comparing list_a ({len(list_a)}) and list_b ({len(list_b)}): {result_ab} - {message_ab}")
    result_ac, message_ac = compare_list_sizes(list_a, list_c)
    print(f"Comparing list_a ({len(list_a)}) and list_c ({len(list_c)}): {result_ac} - {message_ac}")
    result_bc, message_bc = compare_list_sizes(list_b, list_c)
    print(f"Comparing list_b ({len(list_b)}) and list_c ({len(list_c)}): {result_bc} - {message_bc}")