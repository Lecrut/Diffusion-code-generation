def negate_boolean(value):
    if value is not True and value is not False:
        raise ValueError("Input must be a boolean")
    return value is False

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)