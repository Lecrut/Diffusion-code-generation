class BooleanComparator:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def compare_booleans(a, b):
        return BooleanComparator.TRUE if a == b else BooleanComparator.FALSE

if __name__ == '__main__':
    print(BooleanComparator.compare_booleans(True, True))
    print(BooleanComparator.compare_booleans(False, False))
    print(BooleanComparator.compare_booleans(True, False))
    print(BooleanComparator.compare_booleans(False, True))