class ConditionTester:
    def check_or(self, prop1, prop2):
        return prop1 or prop2
if __name__ == '__main__':
    tester = ConditionTester()
    print(tester.check_or(True, False))
    print(tester.check_or(False, False))
    print(tester.check_or(True, True))
    print(tester.check_or(None, True))
    print(tester.check_or(0, True))