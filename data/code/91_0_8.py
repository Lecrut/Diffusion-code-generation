class BooleanNegator:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def _lookup(value):
        table = {True: False, False: True}
        return table[value]

def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return BooleanNegator._lookup(value)

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)