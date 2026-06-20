class ConditionTester:

    def validate_or_condition(self, prop1, prop2):
        return prop1 or prop2
if __name__ == '__main__':
    tester = ConditionTester()
    print(tester.validate_or_condition(True, False))
    print(tester.validate_or_condition(False, False))
    print(tester.validate_or_condition(0, 'hello'))
    print(tester.validate_or_condition('', []))