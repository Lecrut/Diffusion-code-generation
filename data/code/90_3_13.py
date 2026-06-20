class ConditionTester:
    def validate_or_condition(self, a, b):
        if not (isinstance(a, bool) and isinstance(b, bool)):
            raise ValueError("Inputs must be boolean values.")
        return a or b

if __name__ == '__main__':
    tester = ConditionTester()
    value1 = True
    value2 = False
    result = tester.validate_or_condition(value1, value2)
    print(f"Value 1: {value1}")
    print(f"Value 2: {value2}")
    print(f"Result of {value1} or {value2}: {result}")

    try:
        value3 = 0
        value4 = 1
        result2 = tester.validate_or_condition(value3, value4)
    except ValueError as e:
        print(e)