class TruthChecker:
    def __init__(self):
        self.flags = [(True, True), (True, False), (False, True), (False, False)]

    def check_flags(self, flag1: bool, flag2: bool) -> bool:
        return flag1 ^ flag2

    def run_tests(self):
        for flag1, flag2 in self.flags:
            result = self.check_flags(flag1, flag2)
            print(f"Test with ({flag1}, {flag2}): {result}")

if __name__ == '__main__':
    checker = TruthChecker()
    checker.run_tests()