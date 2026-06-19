def are_objects_equal(x, y):
    return x == y
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = [1, 2, 3]
    sample3 = (1, 2, 3)
    sample4 = 'hello'
    print(are_objects_equal(sample1, sample2))
    print(are_objects_equal(sample1, sample3))
    print(are_objects_equal(sample3, sample3))
    print(are_objects_equal(sample4, 'hello'))