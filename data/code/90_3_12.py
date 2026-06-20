class ConditionTester:
    def validate_or_condition(self, a, b):
        return a or b

if __name__ == '__main__':
    tester = ConditionTester()
    result1 = tester.validate_or_condition(True, False)
    print(f"Result of True or False: {result1}")
    
    result2 = tester.validate_or_condition(0, 1)
    print(f"Result of 0 or 1: {result2}")