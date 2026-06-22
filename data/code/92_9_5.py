class TruthNegator:
    def __init__(self):
        self._cache = {True: False, False: True}

    def negate(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return self._cache[value]

def find_opposite_truth(value):
    negator = TruthNegator()
    return negator.negate(value)

if __name__ == '__main__':
    negator_instance = TruthNegator()
    result1 = negator_instance.negate(True)
    result2 = negator_instance.negate(False)
    result3 = find_opposite_truth(True)
    result4 = find_opposite_truth(False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)