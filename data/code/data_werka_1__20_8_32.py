def are_equal(item1, item2):
    return item1 == item2
if __name__ == '__main__':
    int1 = 42
    int2 = 42
    str1 = 'hello'
    str2 = 'world'
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(are_equal(int1, int2))
    print(are_equal(str1, str2))
    print(are_equal(list1, list2))