def are_objects_equal(x, y):
    return x == y
if __name__ == '__main__':
    obj1 = [1, 2, 3]
    obj2 = [1, 2, 3]
    obj3 = 'hello'
    obj4 = 'world'
    print(are_objects_equal(obj1, obj2))
    print(are_objects_equal(obj3, obj4))