def verify_value_equality(a, b):
    return a == b

if __name__ == '__main__':
    sample1 = (5, 5)
    sample2 = (5, '5')
    sample3 = ([1, 2], [1, 2])
    sample4 = ([1, 2], [2, 1])

    print(verify_value_equality(*sample1))
    print(verify_value_equality(*sample2))
    print(verify_value_equality(*sample3))
    print(verify_value_equality(*sample4))