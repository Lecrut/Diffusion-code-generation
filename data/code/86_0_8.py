class BooleanComparator:
    def compare(self, a: bool, b: bool) -> str:
        return "True" if a == b else "False"

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, False))
    print(comparator.compare(False, False))
    print(comparator.compare(True, True))