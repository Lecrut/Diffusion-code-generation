TRUE_CONST = True
FALSE_CONST = False

def negate_boolean(value: bool) -> bool:
    if value is TRUE_CONST:
        return FALSE_CONST
    return TRUE_CONST

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))