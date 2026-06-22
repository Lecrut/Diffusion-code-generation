class NumericComparator:

    def compare(self, a: int, b: int) -> int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
if __name__ == '__main__':
    comparator = NumericComparator()
    print(comparator.compare(5, 3))
    print(comparator.compare(10, 10))
    print(comparator.compare(2, 8))