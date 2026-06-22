class PairVerifier:
    def __init__(self, flag_a: bool, flag_b: bool):
        self.flag_a = flag_a
        self.flag_b = flag_b

    def are_both_false(self) -> bool:
        return not self.flag_a and not self.flag_b

    def are_any_true(self) -> bool:
        return self.flag_a or self.flag_b

if __name__ == '__main__':
    verifier = PairVerifier(False, False)
    print(verifier.are_both_false())
    print(verifier.are_any_true())
    verifier.flag_a = True
    print(verifier.are_both_false())
    print(verifier.are_any_true())