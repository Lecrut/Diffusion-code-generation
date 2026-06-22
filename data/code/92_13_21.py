TRUE_VALUE = True
FALSE_VALUE = False

def invert_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ TRUE_VALUE

if __name__ == '__main__':
    result_true = invert_boolean(True)
    result_false = invert_boolean(False)
    print(result_true)
    print(result_false)