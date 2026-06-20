class FlagCombiner:
    @staticmethod
    def combine_flags(flag1: int, flag2: int) -> int:
        return flag1 | flag2

if __name__ == '__main__':
    test_flag1 = 5
    test_flag2 = 3
    result = FlagCombiner.combine_flags(test_flag1, test_flag2)
    print(result)