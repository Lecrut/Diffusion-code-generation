def check_identity_and_equality(a, b):
    is_none_a = a is None
    is_none_b = b is None
    if is_none_a or is_none_b:
        return a == b
    else:
        return a is b and a == b
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42
    sample3 = None
    sample4 = None
    sample5 = []
    sample6 = []
    sample7 = 'test'
    sample8 = 'test'
    print(check_identity_and_equality(sample1, sample2))
    print(check_identity_and_equality(sample3, sample4))
    print(check_identity_and_equality(sample1, sample3))
    print(check_identity_and_equality(sample5, sample6))
    print(check_identity_and_equality(sample7, sample8))