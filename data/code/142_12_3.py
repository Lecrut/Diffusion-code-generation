class BooleanComparator:
    @staticmethod
    def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
        result = a == b
        if result:
            outcome = "Equal"
        else:
            outcome = "Not Equal"
        return result, outcome
if __name__ == '__main__':
    print(BooleanComparator.compare_booleans(True, True))
    print(BooleanComparator.compare_booleans(True, False))
    print(BooleanComparator.compare_booleans(False, False))
    print(BooleanComparator.compare_booleans(False, True))