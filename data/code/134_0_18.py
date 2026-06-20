class ConditionChecker:

    @staticmethod
    def are_conditions_mutually_exclusive(a: bool, b: bool, c: bool) -> bool:
        return a and (not b) and (not c) or (not a and b and (not c)) or (not a and (not b) and c)
if __name__ == '__main__':
    print(ConditionChecker.are_conditions_mutually_exclusive(True, False, False))
    print(ConditionChecker.are_conditions_mutually_exclusive(False, True, False))
    print(ConditionChecker.are_conditions_mutually_exclusive(False, False, True))
    print(ConditionChecker.are_conditions_mutually_exclusive(True, True, False))
    print(ConditionChecker.are_conditions_mutually_exclusive(True, False, True))
    print(ConditionChecker.are_conditions_mutually_exclusive(False, True, True))
    print(ConditionChecker.are_conditions_mutually_exclusive(True, True, True))