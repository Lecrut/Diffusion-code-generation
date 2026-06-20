def test_or_logical_condition():
    assert True or False == True
    assert False or True == True
    assert False or False == False
    assert 0 or 1 == 1
    assert 1 or 0 == 1
    assert '' or 'text' == 'text'
    assert 'text' or '' == 'text'
    assert [] or [1] == [1]
    assert [1] or [] == [1]
    print("All tests passed.")

if __name__ == '__main__':
    test_or_logical_condition()