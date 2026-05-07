class BooleanNegator:
    def __init__(self, initial_value: bool):
        self._value = initial_value
    def negate(self) -> bool:
        self._value = not self._value
        return self._value
if __name__ == '__main__':
    b1 = BooleanNegator(True)
    print(f"Original value of b1: {b1._value}")
    negated_b1 = b1.negate()
    print(f"Negated value of b1: {negated_b1}")
    b2 = BooleanNegator(False)
    print(f"Original value of b2: {b2._value}")
    negated_b2 = b2.negate()
    print(f"Negated value of b2: {negated_b2}")