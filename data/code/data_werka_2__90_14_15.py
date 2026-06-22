def test_or_condition(a, b):
    result = a or b
    return result

if __name__ == '__main__':
    val1 = 0
    val2 = 42
    output = test_or_condition(val1, val2)
    print(output)