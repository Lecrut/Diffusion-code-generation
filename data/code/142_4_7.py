class BooleanComparator:
    @staticmethod
    def check_xor_difference(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    print(BooleanComparator.check_xor_difference(True, False))
    print(BooleanComparator.check_xor_difference(True, True))
    print(BooleanComparator.check_xor_difference(False, False))
    print(BooleanComparator.check_xor_difference(True, True))
    print(BooleanComparator.check_xor_difference(False, True))