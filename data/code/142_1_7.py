class BooleanComparator:
    TRUE = True
    FALSE = False
    
    @staticmethod
    def are_identical(a: bool, b: bool) -> int:
        return (a - b) & 0x1

if __name__ == '__main__':
    result1 = BooleanComparator.are_identical(True, True)
    print(result1)
    result2 = BooleanComparator.are_identical(False, False)
    print(result2)
    result3 = BooleanComparator.are_identical(True, False)
    print(result3)
    result4 = BooleanComparator.are_identical(False, True)
    print(result4)