class BitmaskChecker:
    @staticmethod
    def is_single_bit_set(mask: int) -> bool:
        return mask != 0 and (mask & (mask - 1)) == 0

if __name__ == '__main__':
    checker = BitmaskChecker()
    flags1 = [False, True, False]
    bitmask1 = sum(2 ** i for i, flag in enumerate(flags1) if flag)
    print(f"Test Case 1: {checker.is_single_bit_set(bitmask1)}")

    flags2 = [True, False, True]
    bitmask2 = sum(2 ** i for i, flag in enumerate(flags2) if flag)
    print(f"Test Case 2: {checker.is_single_bit_set(bitmask2)}")