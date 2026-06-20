class BooleanComparator:
    def compare(self, a: bool, b: bool) -> str:
        return 'Equal' if a == b else 'One is True, the other is False'

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(True, False))
    print(comparator.compare(False, True))
    print(comparator.compare(False, False))