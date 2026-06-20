class BooleanOperations:
    def xor_check(self, a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    checker = BooleanOperations()
    print(checker.xor_check(True, False))
    print(checker.xor_check(False, True))
    print(checker.xor_check(True, True))
    print(checker.xor_check(False, False))