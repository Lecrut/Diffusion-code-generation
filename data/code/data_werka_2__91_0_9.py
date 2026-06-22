TRUE_CONST = True
FALSE_CONST = False
NEGATION_TABLE = {TRUE_CONST: FALSE_CONST, FALSE_CONST: TRUE_CONST}

def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return NEGATION_TABLE[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))