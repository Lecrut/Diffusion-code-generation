class BooleanComparator:
    def compare(self, a: bool, b: bool) -> str:
        if a == b:
            return 'Equal'
        elif a and not b:
            return 'One is True, the other is False'
        elif not a and b:
            return 'One is True, the other is False'
        else:
            return 'Both are False'

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(True, False))
    print(comparator.compare(False, True))
    print(comparator.compare(False, False))