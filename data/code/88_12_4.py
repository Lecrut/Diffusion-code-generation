class BooleanConjunction:
    def check_both_true(self, a: bool, b: bool) -> bool:
        return a & b

if __name__ == '__main__':
    conj = BooleanConjunction()
    print(f"check_both_true(True, True): {conj.check_both_true(True, True)}")
    print(f"check_both_true(False, False): {conj.check_both_true(False, False)}")
    print(f"check_both_true(False, True): {conj.check_both_true(False, True)}")
    print(f"check_both_true(True, False): {conj.check_both_true(True, False)}")