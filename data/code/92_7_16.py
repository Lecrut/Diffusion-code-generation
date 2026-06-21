TRUE_CONSTANT = True
FALSE_CONSTANT = False

def invert_boolean(value: bool) -> bool:
    if value is TRUE_CONSTANT:
        return FALSE_CONSTANT
    return TRUE_CONSTANT

if __name__ == '__main__':
    sample_value = True
    result = invert_boolean(sample_value)
    print(result)
    sample_value = False
    result = invert_boolean(sample_value)
    print(result)