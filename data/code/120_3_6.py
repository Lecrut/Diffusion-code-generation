def are_values_equal(val1, val2):
    return val1 == val2

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(10, 5))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(3.14, 3.1400000000000004))