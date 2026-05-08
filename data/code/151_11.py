def combine_lists(list_a, list_b):
    list_a.extend(list_b)
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combine_lists(list1, list2)
    print(list1)