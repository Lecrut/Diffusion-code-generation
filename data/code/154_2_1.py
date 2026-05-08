def count_items(data_list):
    return len(data_list)
if __name__ == '__main__':
    list1 = [1, "a", 3.14, True]
    list2 = []
    list3 = ["hello", None, []]
    list4 = [5]
    print(count_items(list1))
    print(count_items(list2))
    print(count_items(list3))
    print(count_items(list4))