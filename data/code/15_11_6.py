class ValueChecker:
    def are_equal(self, a, b):
        if a == b:
            return True
        if type(a) != type(b):
            try:
                if str(a) == str(b):
                    return True
            except Exception:
                pass
        return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"10 == 10: {checker.are_equal(10, 10)}")
    print(f"'10' == 10: {checker.are_equal('10', 10)}")
    print(f"10 == 10.0: {checker.are_equal(10, 10.0)}")
    print(f"10 == 10.0: {checker.are_equal(10, 10.0)}")
    print(f"10 == 11: {checker.are_equal(10, 11)}")
    print(f"'10' == 10.0: {checker.are_equal('10', 10.0)}")
    print(f"10 == '10': {checker.are_equal(10, '10')}")
    print(f"True == 1: {checker.are_equal(True, 1)}")
    print(f"False == 0: {checker.are_equal(False, 0)}")
    print(f"None == None: {checker.are_equal(None, None)}")
    print(f"None == 0: {checker.are_equal(None, 0)}")
    print(f"5.0 == 5: {checker.are_equal(5.0, 5)}")
    print(f"5.0 == 6: {checker.are_equal(5.0, 6)}")