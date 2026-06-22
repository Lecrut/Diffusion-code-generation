TRUE_VAL = True
FALSE_VAL = False

def invert_boolean(value: bool) -> bool:
    if value is TRUE_VAL:
        return FALSE_VAL
    return TRUE_VAL

if __name__ == '__main__':
    sample_value = True
    result = invert_boolean(sample_value)
    print(result)
    sample_value = False
    result = invert_boolean(sample_value)
    print(result)