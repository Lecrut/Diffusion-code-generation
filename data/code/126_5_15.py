def verify_value_equality(a, b):
    if type(a) != type(b):
        raise ValueError("Inputs must be of the same type")
    return a == b

if __name__ == '__main__':
    try:
        print(verify_value_equality(5, 5))
        print(verify_value_equality(5, '5'))
        print(verify_value_equality([1, 2], [1, 2]))
        print(verify_value_equality([1, 2], [2, 1]))
    except ValueError as e:
        print(e)