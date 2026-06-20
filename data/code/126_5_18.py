def verify_value_equality(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 42
    value2 = '42'
    result = verify_value_equality(value1, value2)
    print(result)