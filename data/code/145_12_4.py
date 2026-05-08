class BooleanTester:
    def test_expression(self, condition1, condition2, nested_logic):
        result = False
        if condition1:
            if condition2:
                if nested_logic:
                    result = True
        return result
if __name__ == '__main__':
    tester = BooleanTester()
    c1_1 = True
    c2_1 = True
    nl_1 = True
    print(f"Test 1 (T, T, T): {tester.test_expression(c1_1, c2_1, nl_1)}")
    c1_2 = True
    c2_2 = False
    nl_2 = True
    print(f"Test 2 (T, F, T): {tester.test_expression(c1_2, c2_2, nl_2)}")
    c1_3 = False
    c2_3 = True
    nl_3 = True
    print(f"Test 3 (F, T, T): {tester.test_expression(c1_3, c2_3, nl_3)}")
    c1_4 = False
    c2_4 = False
    nl_4 = False
    print(f"Test 4 (F, F, F): {tester.test_expression(c1_4, c2_4, nl_4)}")
    c1_5 = True
    c2_5 = False
    nl_5 = False
    print(f"Test 5 (T, F, F): {tester.test_expression(c1_5, c2_5, nl_5)}")