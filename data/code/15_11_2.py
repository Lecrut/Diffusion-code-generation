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
    print(f"10 == 10.0: {checker.are_equal(10, 10.0)}")
    print(f"10 == 10.1: {checker.are_equal(10, 10.1)}")
    print(f"'10' == 10.0: {checker.are_equal('10', 10.0)}")
    print(f"10 == 11: {checker.are_equal(10, 11)}")
    print(f"None == None: {checker.are_equal(None, None)}")
    print(f"None == 0: {checker.are_equal(None, 0)}")
    print(f"5.0 == 5: {checker.are_equal(5.0, 5)}")
    print(f"'5.0' == 5: {checker.are_equal('5.0', 5)}")
    print(f"'5.0' == 5.0: {checker.are_equal('5.0', 5.0)}")
    print(f"True == 1: {checker.are_equal(True, 1)}")
    print(f"False == 0: {checker.are_equal(False, 0)}")
    print(f"True == 'True': {checker.are_equal(True, 'True')}")
    print(f"1.0 == 1: {checker.are_equal(1.0, 1)}")
    print(f"1.0 == 1.0000000000000001: {checker.are_equal(1.0, 1.0000000000000001)}")
    print(f"1.0 == 1.000000000000001: {checker.are_equal(1.0, 1.000000000000001)}")
    print(f"1.0 == 1.000000000000002: {checker.are_equal(1.0, 1.000000000000002)}")