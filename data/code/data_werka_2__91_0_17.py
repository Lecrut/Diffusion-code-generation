def negate_boolean(flag):
    if not isinstance(flag, bool):
        raise ValueError("Argument must be a boolean type")
    _table = {True: False, False: True}
    return _table[flag]

if __name__ == '__main__':
    val1 = True
    val2 = False
    print(negate_boolean(val1))
    print(negate_boolean(val2))