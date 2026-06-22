def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    first_value = 42
    second_value = 42
    third_value = [1, 2, 3]
    fourth_value = [3, 2, 1]
    
    print(is_equal(first_value, second_value))  # True
    print(is_equal(third_value, fourth_value))  # False
    print(is_equal("hello", "hello"))         # True
    print(is_equal({"key": 1}, {"key": 1}))     # True