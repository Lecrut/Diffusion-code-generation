def test_or_condition(a, b):
    result = a or b
    return result

if __name__ == '__main__':
    val_a = 0
    val_b = 42
    output = test_or_condition(val_a, val_b)
    print(output)