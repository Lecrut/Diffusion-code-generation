def are_objects_equal(x, y):
    return x == y

if __name__ == '__main__':
    list1 = [4, 5, 6]
    list2 = [4, 5, 6]
    tuple1 = (7, 8, 9)
    string1 = 'world'
    string2 = 'world'

    print(are_objects_equal(list1, list2))
    print(are_objects_equal(list1, tuple1))
    print(are_objects_equal(string1, string2))
    print(are_objects_equal(tuple1, (7, 8, 9)))