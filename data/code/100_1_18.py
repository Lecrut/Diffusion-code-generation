class LogicChecker:
    @staticmethod
    def check_logic(A, B, C):
        return A and (B or not C)

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.check_logic(True, False, True))
    print(checker.check_logic(False, True, False))
    print(checker.check_logic(True, True, False))
    print(checker.check_logic(False, False, False))