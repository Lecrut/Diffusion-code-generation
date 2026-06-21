def invert_boolean(value: bool) -> bool:
    if value is True:
        return False
    return True

if __name__ == '__main__':
    sample_value = True
    result = invert_boolean(sample_value)
    print(result)
    sample_value = False
    result = invert_boolean(sample_value)
    print(result)