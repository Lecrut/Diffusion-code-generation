TRUE_NEGATION = False
FALSE_NEGATION = True

NEGATION_TABLE = {
    True: TRUE_NEGATION,
    False: FALSE_NEGATION
}

def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return NEGATION_TABLE[value]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))