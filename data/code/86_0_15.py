class BooleanComparator:
    TRUE = "True"
    FALSE = "False"

    @staticmethod
    def compare(a: bool, b: bool) -> str:
        return BooleanComparator.TRUE if a == b else BooleanComparator.FALSE

if __name__ == '__main__':
    print(BooleanComparator.compare(True, False))
    print(BooleanComparator.compare(False, False))
    print(BooleanComparator.compare(True, True))