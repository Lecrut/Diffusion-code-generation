def verify_value_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(verify_value_equality(5, 5))
    print(verify_value_equality(5, '5'))
    print(verify_value_equality([1, 2], [1, 2]))
    print(verify_value_equality([1, 2], (1, 2)))