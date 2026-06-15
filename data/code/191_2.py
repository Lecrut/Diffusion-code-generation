def merge_lists(list1, list2):
    list1.extend(list2)
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    merge_lists(list_a, list_b)
    print(list_a)