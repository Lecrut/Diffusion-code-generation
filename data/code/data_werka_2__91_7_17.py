class BooleanNegator:
    TRUTH_TABLE = {True: False, False: True}

    @staticmethod
    def get_negation(value):
        if value not in BooleanNegator.TRUTH_TABLE:
            raise ValueError("Input must be a boolean value")
        return BooleanNegator.TRUTH_TABLE[value]

    def __init__(self, initial_value):
        if not isinstance(initial_value, bool):
            raise ValueError("Initial value must be a boolean")
        self.value = initial_value

    def negate(self):
        self.value = BooleanNegator.get_negation(self.value)
        return self.value

if __name__ == '__main__':
    negator = BooleanNegator(True)
    result = negator.negate()
    print(result)