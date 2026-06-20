class BooleanComparator:
    @staticmethod
    def check_xor_difference(a: bool, b: bool) -> bool:
        return a ^ b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_xor_difference(True, False))
    print(comparator.check_xor_difference(True, True))
    print(comparator.check_xor_difference(False, False))
    print(comparator.check_xor_difference(True, True))
    print(comparator.check_xor_difference(False, True))