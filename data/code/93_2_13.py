class BooleanChecker:

    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and (not b)
if __name__ == '__main__':
    bc = BooleanChecker()
    print(bc.check_both_false(False, False))
    print(bc.check_both_false(True, False))
    print(bc.check_both_false(False, True))
    print(bc.check_both_false(True, True))