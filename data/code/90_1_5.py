class ConditionChecker:
    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    checker = ConditionChecker()
    print(f"check_or_condition(True, False): {checker.check_or_condition(True, False)}")
    print(f"check_or_condition(False, True): {checker.check_or_condition(False, True)}")
    print(f"check_or_condition(True, True): {checker.check_or_condition(True, True)}")
    print(f"check_or_condition(False, False): {checker.check_or_condition(False, False)}")