class BooleanNegator:
    def __init__(self):
        self.table = {True: False, False: True}

    def negate(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self.table[value]

def negate_boolean(value):
    negator = BooleanNegator()
    return negator.negate(value)

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)