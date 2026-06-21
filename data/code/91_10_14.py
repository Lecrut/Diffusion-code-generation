TRUE_VAL = True
FALSE_VAL = False

def negate_boolean(value):
    if value == TRUE_VAL:
        return FALSE_VAL
    if value == FALSE_VAL:
        return TRUE_VAL
    raise ValueError("Input must be a boolean")

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))