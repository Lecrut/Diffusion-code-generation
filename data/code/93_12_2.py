class BooleanChecker:
    def are_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b
if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"are_both_false(False, False): {checker.are_both_false(False, False)}")
    print(f"are_both_false(False, True): {checker.are_both_false(False, True)}")
    print(f"are_both_false(True, False): {checker.are_both_false(True, False)}")
    print(f"are_both_false(True, True): {checker.are_both_false(True, True)}")