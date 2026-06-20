class BooleanComparator:
    @staticmethod
    def xnor(a: bool, b: bool) -> bool:
        return not (a ^ b)

if __name__ == '__main__':
    result1 = BooleanComparator.xnor(True, True)
    print(result1)
    result2 = BooleanComparator.xnor(False, False)
    print(result2)
    result3 = BooleanComparator.xnor(True, False)
    print(result3)
    result4 = BooleanComparator.xnor(False, True)
    print(result4)