class CheckCombiner:
    @staticmethod
    def combine_checks(a, b, c):
        return a > 0 and b % 2 == 0 and c % a == 0

if __name__ == '__main__':
    combiner = CheckCombiner()
    print(combiner.combine_checks(3, 4, 12))
    print(combiner.combine_checks(5, 6, 10))
    print(combiner.combine_checks(2, 8, 10))
    print(combiner.combine_checks(-1, 4, 2))
    print(combiner.combine_checks(1, 5, 10))