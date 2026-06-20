def flip_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_value = False
    result = flip_boolean(test_value)
    print(result)