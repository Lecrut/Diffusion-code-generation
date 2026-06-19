def are_objects_equal(x, y):
    return x == y
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 4]
    print(are_objects_equal(a, b))
    print(are_objects_equal(a, c))