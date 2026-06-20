class BooleanComparator:
    def compare(self, a: bool, b: bool) -> tuple[bool, str]:
        result = a == b
        operation = "=="
        return (result, operation)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(True, False))
    print(comparator.compare(False, False))
    print(comparator.compare(False, True))