def invert_boolean(value: bool) -> bool:
    TRUE_CONSTANT = True
    FALSE_CONSTANT = False
    return FALSE_CONSTANT if value is TRUE_CONSTANT else TRUE_CONSTANT

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    print(invert_boolean(sample_true))
    print(invert_boolean(sample_false))