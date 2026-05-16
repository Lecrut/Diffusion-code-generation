def combine_lists_extend(list_a, list_b):
    list_a.extend(list_b)
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Before combining:")
    print("List A:", list1)
    print("List B:", list2)
    combine_lists_extend(list1, list2)
    print("After combining (List A modified in place):")
    print("List A:", list1)