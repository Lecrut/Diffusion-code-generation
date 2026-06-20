class ConditionTester:

    def validate_or_condition(self, prop1, prop2):
        return prop1 or prop2
if __name__ == '__main__':
    tester = ConditionTester()
    result = tester.validate_or_condition(True, False)
    print(result)