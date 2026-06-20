class BooleanFlagComparator:
    def compare_flags(self, flag1: bool, flag2: bool) -> bool:
        return flag1 == flag2

if __name__ == '__main__':
    comparator = BooleanFlagComparator()
    print(comparator.compare_flags(True, True))
    print(comparator.compare_flags(False, False))
    print(comparator.compare_flags(True, False))
    print(comparator.compare_flags(False, True))