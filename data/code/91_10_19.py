def negate_boolean(value):
    if value is True:
        return False
    return True

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)