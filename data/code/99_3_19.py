def test_boolean_expressions():
    result = (True and False) or (not True) == False and 5 > 3
    return result

if __name__ == '__main__':
    print(test_boolean_expressions())