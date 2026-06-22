TRUE_VAL = True
FALSE_VAL = False

NEGATION_TABLE = {
    True: False,
    False: True
}

def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return NEGATION_TABLE[value]

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)