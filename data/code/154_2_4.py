def count_items(data_list):
    return len(data_list)
if __name__ == '__main__':
    list1 = [1, "a", 3.14, True]
    list2 = []
    list3 = ["hello", None, []]
    list4 = [100]
    print(f"Count for list1: {count_items(list1)}")
    print(f"Count for list2: {count_items(list2)}")
    print(f"Count for list3: {count_items(list3)}")
    print(f"Count for list4: {count_items(list4)}")