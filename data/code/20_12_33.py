def check_equality(item1, item2):
    return item1 is item2 and item1 == item2
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    print(check_equality(list1, list2))
    print(check_equality(list1, list3))