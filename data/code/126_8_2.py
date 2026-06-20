def are_values_equal(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal(5, 6))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal("hello", "world"))