class BooleanComparator:

    def xnor(self, a: bool, b: bool) -> bool:
        return not a ^ b
if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.xnor(True, True)
    print(result1)
    result2 = comparator.xnor(False, False)
    print(result2)
    result3 = comparator.xnor(True, False)
    print(result3)
    result4 = comparator.xnor(False, True)
    print(result4)