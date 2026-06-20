class BooleanComparator:
    TRUE = "True"
    FALSE = "False"

    @staticmethod
    def compare_booleans(a: bool, b: bool) -> str:
        return BooleanComparator.TRUE if a == b else BooleanComparator.FALSE

if __name__ == '__main__':
    result1 = BooleanComparator.compare_booleans(True, False)
    print(result1)

    result2 = BooleanComparator.compare_booleans(False, False)
    print(result2)

    result3 = BooleanComparator.compare_booleans(True, True)
    print(result3)