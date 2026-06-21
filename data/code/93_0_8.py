def both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError(f"a must be a boolean, got {type(a)}")
    if not isinstance(b, bool):
        raise ValueError(f"b must be a boolean, got {type(b)}")
    return not a and not b

class BooleanChecker:
    def __init__(self, val1: bool, val2: bool):
        self.val1 = val1
        self.val2 = val2

    def check(self) -> bool:
        if not isinstance(self.val1, bool):
            raise ValueError(f"val1 must be a boolean, got {type(self.val1)}")
        if not isinstance(self.val2, bool):
            raise ValueError(f"val2 must be a boolean, got {type(self.val2)}")
        return not self.val1 and not self.val2

if __name__ == '__main__':
    result1 = both_false(False, False)
    print(result1)

    checker = BooleanChecker(False, False)
    result2 = checker.check()
    print(result2)