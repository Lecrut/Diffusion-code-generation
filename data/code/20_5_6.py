class NumberChecker:
    MODUS_EVEN = 2

    @staticmethod
    def check_even(value):
        return True if value % NumberChecker.MODUS_EVEN == 0 else False

if __name__ == '__main__':
    print(NumberChecker.check_even(1024))
    print(NumberChecker.check_even(753))
    print(NumberChecker.check_even(-22))
    print(NumberChecker.check_even(0))