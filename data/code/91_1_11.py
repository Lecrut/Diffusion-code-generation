class BooleanNegator:
    _negation_table = {True: False, False: True}

    @classmethod
    def negate(cls, value):
        return cls._negation_table.get(value)

if __name__ == '__main__':
    negator_instance = BooleanNegator()
    result1 = negator_instance.negate(True)
    result2 = negator_instance.negate(False)
    print(result1)
    print(result2)