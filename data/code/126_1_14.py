def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal([1, 2, 3], [1, 2, 3]))
    print(are_values_equal((4, 5), (4, 5)))
    print(are_values_equal({"a": 1}, {"a": 1}))