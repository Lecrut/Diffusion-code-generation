def invert_boolean(flag):
    mapping = {True: False, False: True}
    if flag not in mapping:
        raise ValueError("Expected a boolean value")
    return mapping[flag]

if __name__ == '__main__':
    true_result = invert_boolean(True)
    false_result = invert_boolean(False)
    print(true_result)
    print(false_result)