def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    print(check_equality(5, 5))          # True
    print(check_equality("foo", "bar"))  # False
    print(check_equality([1, 2], [1, 2]))# True
    print(check_equality({"a": 1}, {"a": 2}))# False