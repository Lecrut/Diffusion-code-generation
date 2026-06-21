class BooleanChecker:
    _truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }

    def check_both_false(self, a: bool, b: bool) -> bool:
        return self._truth_table[(bool(a), bool(b))]

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.check_both_false(False, False))
    print(checker.check_both_false(False, True))
    print(checker.check_both_false(True, False))
    print(checker.check_both_false(True, True))