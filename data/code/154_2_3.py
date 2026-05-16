def count_items(data):
    return len(data)
if __name__ == '__main__':
    list1 = [1, "a", 3.14, True]
    list2 = []
    list3 = ["hello", None, [1, 2]]
    list4 = []
    print(count_items(list1))
    print(count_items(list2))
    print(count_items(list3))
    print(count_items(list4))