class DualBooleanChecker:
    _FALSE_INDICATORS = {
        False: 0,
        True: 1,
    }

    def __init__(self, value_a: bool, value_b: bool):
        self.value_a = value_a
        self.value_b = value_b

    def are_both_false(self) -> bool:
        indicator_a = self._FALSE_INDICATORS.get(self.value_a, -1)
        indicator_b = self._FALSE_INDICATORS.get(self.value_b, -1)
        if indicator_a == -1 or indicator_b == -1:
            raise ValueError("Attributes must be boolean")
        return indicator_a == 0 and indicator_b == 0

if __name__ == '__main__':
    checker = DualBooleanChecker(False, False)
    result = checker.are_both_false()
    print(result)