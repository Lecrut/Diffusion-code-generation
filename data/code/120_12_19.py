def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    print(check_equality(20, 20))
    print(check_equality(20.0, 20))
    print(check_equality(20, 20.0))
    print(check_equality("test", "test"))
    print(check_equality("test", "sample"))
    print(check_equality(2.718, 2.7180000000000002))
    print(check_equality([3], [3]))