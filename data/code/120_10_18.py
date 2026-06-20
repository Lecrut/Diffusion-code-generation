def are_equal(a, b):
    if type(a) is not type(b):
        return False
    return a is b

if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal(10, 5))
    print(are_equal("hello", "hello"))
    print(are_equal([1, 2], [1, 2]))