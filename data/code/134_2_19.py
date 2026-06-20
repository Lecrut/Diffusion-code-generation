class ExclusiveConditionChecker:
    def __init__(self, a: bool, b: bool, c: bool, d: bool):
        self.conditions = (a, b, c, d)

    def is_exclusive(self) -> bool:
        return sum(self.conditions) == 1

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, False, True)
    print(checker.is_exclusive())