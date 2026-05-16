class BooleanTester:
    def test_expression(self, condition1, condition2, nested_logic):
        if condition1 and condition2:
            if nested_logic:
                return True
            else:
                return False
        else:
            return False
if __name__ == '__main__':
    tester = BooleanTester()
    result1 = tester.test_expression(True, True, True)
    print(f"Test 1 Result: {result1}")
    result2 = tester.test_expression(True, True, False)
    print(f"Test 2 Result: {result2}")
    result3 = tester.test_expression(True, False, True)
    print(f"Test 3 Result: {result3}")
    result4 = tester.test_expression(False, True, True)
    print(f"Test 4 Result: {result4}")
    result5 = tester.test_expression(False, False, True)
    print(f"Test 5 Result: {result5}")
    result6 = tester.test_expression(False, False, False)
    print(f"Test 6 Result: {result6}")