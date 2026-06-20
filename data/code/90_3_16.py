class ConditionTester:
    TRUE = True
    FALSE = False

    def validate_or_condition(self, prop1, prop2):
        return prop1 or prop2

if __name__ == '__main__':
    tester = ConditionTester()
    value1 = tester.TRUE
    value2 = tester.FALSE
    print(f"Value 1: {value1}")
    print(f"Value 2: {value2}")
    result = tester.validate_or_condition(value1, value2)
    print(f"Result of {value1} or {value2}: {result}")