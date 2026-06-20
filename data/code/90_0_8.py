def test_or_logical_condition():
    assert True or False == True
    assert False or True == True
    assert True or True == True
    assert False or False == False

if __name__ == '__main__':
    print(test_or_logical_condition())