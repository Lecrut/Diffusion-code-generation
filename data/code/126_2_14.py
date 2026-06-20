def check_equality(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    result1 = check_equality(42, 42)
    result2 = check_equality('world', 'hello')
    result3 = check_equality([1, 2], [1, 2])
    result4 = check_equality(None, None)
    print(result1)
    print(result2)
    print(result3)
    print(result4)