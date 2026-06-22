def invert_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_value = False
    result = invert_boolean(sample_value)
    print(result)
    sample_value = True
    result = invert_boolean(sample_value)
    print(result)