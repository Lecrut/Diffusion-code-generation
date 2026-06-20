class BooleanComparator:
    @staticmethod
    def xnor(a: bool, b: bool) -> bool:
        return not (a ^ b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.xnor(True, True))
    print(comparator.xnor(False, False))
    print(comparator.xnor(True, False))
    print(comparator.xnor(False, True))