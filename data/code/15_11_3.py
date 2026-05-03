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
    print(f"10 == 10.00000000000001: {checker.are_equal(10, 10.00000000000001)}")
    print(f"10 == 10.00000000000002: {checker.are_equal(10, 10.00000000000002)}")
    print(f"'10' == '10': {checker.are_equal('10', '10')}")
    print(f"'10.0' == '10': {checker.are_equal('10.0', '10')}")
    print(f"'10.0' == 10: {checker.are_equal('10.0', 10)}")
    print(f"10 == 10.00000000000001: {checker.are_equal(10, 10.00000000000001)}")
    print(f"10 == 10.00000000000002: {checker.are_equal(10, 10.00000000000002)}")
    print(f"10.0 == 10.00000000000001: {checker.are_equal(10.0, 10.00000000000001)}")
    print(f"10.0 == 10.00000000000002: {checker.are_equal(10.0, 10.00000000000002)}")
    print(f"10.00000000000001 == 10.00000000000002: {checker.are_equal(10.00000000000001, 10.00000000000002)}")
    print(f"10.00000000000002 == 10.00000000000001: {checker.are_equal(10.00000000000002, 10.00000000000001)}")
    print(f"10 == 100: {checker.are_equal(10, 100)}")
    print(f"'a' == 'b': {checker.are_equal('a', 'b')}")
    print(f"None == None: {checker.are_equal(None, None)}")
    print(f"None == 0: {checker.are_equal(None, 0)}")
    print(f"None == 0.0: {checker.are_equal(None, 0.0)}")
    print(f"'10.5' == 10.5: {checker.are_equal('10.5', 10.5)}")
    print(f"'10.5' == 10.500000000000002: {checker.are_equal('10.5', 10.500000000000002)}")