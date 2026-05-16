class ValueChecker:
    def are_equal(self, a, b):
        if a == b:
            return True
        if type(a) != type(b):
            try:
                return float(a) == float(b)
            except (ValueError, TypeError):
                return False
        return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"10 == 10: {checker.are_equal(10, 10)}")
    print(f"'10' == 10: {checker.are_equal('10', 10)}")
    print(f"10.0 == 10: {checker.are_equal(10.0, 10)}")
    print(f"10.0 == 10: {checker.are_equal(10.0, 10)}")
    print(f"10 == 10.0: {checker.are_equal(10, 10.0)}")
    print(f"10 == 11: {checker.are_equal(10, 11)}")
    print(f"'10' == 11: {checker.are_equal('10', 11)}")
    print(f"10.5 == 10.5: {checker.are_equal(10.5, 10.5)}")
    print(f"10.5 == 10: {checker.are_equal(10.5, 10)}")
    print(f"'10.5' == 10.5: {checker.are_equal('10.5', 10.5)}")
    print(f"10 == '10': {checker.are_equal(10, '10')}")
    print(f"10 == 'abc': {checker.are_equal(10, 'abc')}")
    print(f"None == None: {checker.are_equal(None, None)}")
    print(f"None == 0: {checker.are_equal(None, 0)}")
    print(f"None == 'None': {checker.are_equal(None, 'None')}")
    print(f"5.0 == 5: {checker.are_equal(5.0, 5)}")
    print(f"5.0 == 5.1: {checker.are_equal(5.0, 5.1)}")
    print(f"'5.0' == 5.0: {checker.are_equal('5.0', 5.0)}")
    print(f"'5.0' == 5.1: {checker.are_equal('5.0', 5.1)}")