def invert_bool_bitwise(flag):
    if flag is True:
        return False
    if flag is False:
        return True
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(invert_bool_bitwise(True))
    print(invert_bool_bitwise(False))