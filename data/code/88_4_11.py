class LogicalAndChecker:
    def check(self, val1: bool, val2: bool) -> bool:
        return val1 and val2

if __name__ == '__main__':
    checker = LogicalAndChecker()
    print(checker.check(True, True))
    print(checker.check(True, False))
    print(checker.check(False, True))
    print(checker.check(False, False))