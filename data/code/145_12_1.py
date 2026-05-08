class BooleanTester:
    def test_expression(self, condition1, condition2, nested_logic):
        result1 = condition1 and condition2
        result2 = result1 or nested_logic
        return result2
if __name__ == '__main__':
    tester = BooleanTester()
    c1 = True
    c2 = False
    nl = True
    final_result = tester.test_expression(c1, c2, nl)
    print(final_result)