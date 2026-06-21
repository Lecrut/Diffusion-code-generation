class BooleanNegator:
    TRUE_VAL = 1
    FALSE_VAL = 0
    NEGATION_TABLE = {True: False, False: True}

    def __init__(self):
        self.cache = {}

    def negate(self, value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        if value in self.cache:
            return self.cache[value]
        result = self.NEGATION_TABLE[value]
        self.cache[value] = result
        return result

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.negate(True))
    print(negator.negate(False))
    print(negator.negate(True))
    print(negator.negate(False))