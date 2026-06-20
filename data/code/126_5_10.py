def verify_value_equality(a, b):
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    print(verify_value_equality(5, 5))
    print(verify_value_equality(5, '5'))
    print(verify_value_equality([1, 2], [1, 2]))
    print(verify_value_equality([1, 2], [2, 1]))