class BooleanOperations:
    @staticmethod
    def xor_check(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    print(BooleanOperations.xor_check(True, False))
    print(BooleanOperations.xor_check(False, True))
    print(BooleanOperations.xor_check(True, True))
    print(BooleanOperations.xor_check(False, False))