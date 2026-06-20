class FlagChecker:
    TRUE_FLAG = 1

    @staticmethod
    def are_flags_true(flag1, flag2):
        return (flag1 & FlagChecker.TRUE_FLAG) == FlagChecker.TRUE_FLAG and \
               (flag2 & FlagChecker.TRUE_FLAG) == FlagChecker.TRUE_FLAG

if __name__ == '__main__':
    print(FlagChecker.are_flags_true(3, 5))
    print(FlagChecker.are_flags_true(4, 6))