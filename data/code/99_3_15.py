def test_boolean_expressions():
    result = (True or False) and (not True == False)
    return result
if __name__ == '__main__':
    print(test_boolean_expressions())