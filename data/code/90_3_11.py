class ConditionTester:
    def validate_properties(self, prop1, prop2):
        if not (isinstance(prop1, bool) or isinstance(prop2, bool)):
            return False
        return True

    def check_or_condition(self, prop1, prop2):
        if not self.validate_properties(prop1, prop2):
            raise ValueError("Both properties must be boolean-like.")
        return prop1 or prop2

if __name__ == '__main__':
    tester = ConditionTester()
    value1 = True
    value2 = False
    result = tester.check_or_condition(value1, value2)
    print(f"Result of {value1} or {value2}: {result}")
    
    value3 = 0
    value4 = 1
    try:
        result2 = tester.check_or_condition(value3, value4)
        print(f"Result of {value3} or {value4}: {result2}")
    except ValueError as e:
        print(e)