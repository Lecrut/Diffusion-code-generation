def invert_bool(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_value = True
    result = invert_bool(test_value)
    print(result)