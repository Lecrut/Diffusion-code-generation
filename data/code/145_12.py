class BooleanTester:
    def test_expression(self, condition1, condition2, nested_logic):
        result1 = condition1 and condition2
        result2 = nested_logic
        final_result = result1 and result2
        return final_result
if __name__ == '__main__':
    tester = BooleanTester()
    c1 = True
    c2 = False
    nl = True
    result = tester.test_expression(c1, c2, nl)
    print(result)