class ConditionTester:
    def validate_or_condition(self, prop1, prop2):
        return bool(prop1) or bool(prop2)

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

    value5 = "hello"
    value6 = ""
    print(f"\nValue 5: '{value5}'")
    print(f"Value 6: '{value6}'")
    result3 = tester.validate_or_condition(value5, value6)
    print(f"Result of '{value5}' or '{value6}': {result3}")