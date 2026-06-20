def test_boolean_expressions():
    result = (True and False) or (not True) and (2 > 1)
    return result

if __name__ == '__main__':
    print(test_boolean_expressions())