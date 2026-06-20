class FlagCombiner:

    def combine_flags(self, flag1, flag2):
        return flag1 | flag2
if __name__ == '__main__':
    combiner = FlagCombiner()
    result1 = combiner.combine_flags(5, 3)
    print(result1)