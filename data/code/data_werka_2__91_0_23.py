class BooleanNegator:
    def __init__(self):
        self._cache = {True: False, False: True}

    def negate(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._cache[value]

def negate_boolean(value):
    negator = BooleanNegator()
    return negator.negate(value)

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))
    print(negate_boolean(True))
    print(negate_boolean(False))