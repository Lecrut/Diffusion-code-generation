class TwoInputLogicChecker:
    def __init__(self):
        self.operator_name = "AND"

    def check(self, val1, val2):
        if not isinstance(val1, bool) or not isinstance(val2, bool):
            raise ValueError("Inputs must be boolean")
        return val1 and val2

    def get_operator(self):
        return self.operator_name

if __name__ == '__main__':
    checker = TwoInputLogicChecker()
    print(checker.get_operator())
    print(checker.check(True, True))
    print(checker.check(True, False))
    print(checker.check(False, True))
    print(checker.check(False, False))