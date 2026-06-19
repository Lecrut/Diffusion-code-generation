def are_equal(a, b):
    return type(a) == type(b) and a == b
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42.0
    sample3 = 'hello'
    sample4 = 'hello'
    sample5 = [1, 2, 3]
    sample6 = [1, 2, 3]
    print(are_equal(sample1, sample2))
    print(are_equal(sample3, sample4))
    print(are_equal(sample5, sample6))