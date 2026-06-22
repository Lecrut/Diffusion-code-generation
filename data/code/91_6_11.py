TRUE_VALUE = 1
FALSE_VALUE = 0
BOOLEAN_MAP = {True: TRUE_VALUE, False: FALSE_VALUE}
INVERSE_MAP = {TRUE_VALUE: False, FALSE_VALUE: True}

def negate_boolean(value: bool) -> bool:
    numeric = BOOLEAN_MAP[value]
    inverted_numeric = numeric ^ TRUE_VALUE
    return INVERSE_MAP[inverted_numeric]

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)