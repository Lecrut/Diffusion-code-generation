def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    first_value = [1, 2, 3]
    second_value = [1, 2, 3]
    third_value = "example"
    fourth_value = "test"
    
    print(is_equal(first_value, second_value))  # True
    print(is_equal(third_value, fourth_value))  # False
    print(is_equal(42, 42.0))                # True
    print(is_equal({"key": "value"}, {"key": "value"}))  # True