def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    test_value = 12
    result = feet_to_inches(test_value)
    assert result == 144
    print(result)