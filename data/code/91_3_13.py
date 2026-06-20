def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_value = True
    result = negate_boolean(test_value)
    print(result)