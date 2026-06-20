class BitmaskChecker:
    def is_mutually_exclusive(self, flags: list[bool]) -> bool:
        bitmask = 0
        for flag in flags:
            if flag:
                bitmask |= 1
            bitmask <<= 1
        return bitmask != 0 and (bitmask & (bitmask - 1)) == 0

if __name__ == '__main__':
    checker = BitmaskChecker()
    flags1 = [False, True, False]
    print(f"Test Case 1: {checker.is_mutually_exclusive(flags1)}")
    flags2 = [True, False, True]
    print(f"Test Case 2: {checker.is_mutually_exclusive(flags2)}")
    flags3 = [False, False, False]
    print(f"Test Case 3: {checker.is_mutually_exclusive(flags3)}")