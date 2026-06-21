def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    print(check_equality(10, 10))          # True
    print(check_equality("hello", "world"))  # False
    print(check_equality([1, 2], [1, 2]))    # True
    print(check_equality({"a": 1}, {"b": 1}))# False