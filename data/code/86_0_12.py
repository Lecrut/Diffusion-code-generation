class BoolComparator:
    TRUE = "True"
    FALSE = "False"

    @staticmethod
    def compare(a: bool, b: bool) -> str:
        return BoolComparator.TRUE if a == b else BoolComparator.FALSE

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.compare(True, False))
    print(comparator.compare(False, False))
    print(comparator.compare(True, True))