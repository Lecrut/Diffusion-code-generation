class ConditionTester:
    @staticmethod
    def validate_or_condition(a, b):
        return a or b

if __name__ == '__main__':
    tester = ConditionTester()
    value1 = True
    value2 = False
    print(f"Value 1: {value1}")
    print(f"Value 2: {value2}")
    result = tester.validate_or_condition(value1, value2)
    print(f"Result of {value1} or {value2}: {result}")

    value3 = 0
    value4 = 1
    print(f"\nValue 3: {value3}")
    print(f"Value 4: {value4}")
    result2 = tester.validate_or_condition(value3, value4)
    print(f"Result of {value3} or {value4}: {result2}")