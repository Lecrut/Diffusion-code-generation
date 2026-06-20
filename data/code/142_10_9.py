class BooleanComparator:
    def compare_booleans(self, a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")
        return (not a) == (not b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare_booleans(True, True))
    print(comparator.compare_booleans(False, False))
    print(comparator.compare_booleans(True, False))