from typing import Tuple

class BooleanChecker:
    def __init__(self, val1: bool, val2: bool):
        if not isinstance(val1, bool):
            raise ValueError("val1 must be a boolean")
        if not isinstance(val2, bool):
            raise ValueError("val2 must be a boolean")
        self.val1 = val1
        self.val2 = val2

    def are_both_false(self) -> bool:
        return not self.val1 and not self.val2

def check_boolean_pair(a: bool, b: bool) -> bool:
    checker = BooleanChecker(a, b)
    return checker.are_both_false()

if __name__ == '__main__':
    result = check_boolean_pair(False, False)
    print(result)