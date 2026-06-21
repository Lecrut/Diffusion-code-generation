def check_equality(a, b):
    result = (a == b)
    return result

if __name__ == '__main__':
    x = [1, 2, 3]
    y = [1, 2, 4]
    z = "test"
    w = "test"
    
    print(check_equality(x, y))  # False
    print(check_equality(z, w))  # True
    print(check_equality(5.0, 5))  # True
    print(check_equality({"key": "value"}, {"key": "value"}))  # True