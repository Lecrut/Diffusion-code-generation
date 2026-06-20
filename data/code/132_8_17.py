class FlagCombiner:
    @staticmethod
    def combine_flags(flag1, flag2):
        return flag1 | flag2

if __name__ == '__main__':
    combiner = FlagCombiner()
    print(combiner.combine_flags(5, 3))
    print(combiner.combine_flags(8, 3))