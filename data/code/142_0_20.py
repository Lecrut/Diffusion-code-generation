class BooleanComparator:
    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    result1 = comparator.compare(True, False)
    result2 = comparator.compare(False, False)
    result3 = comparator.compare(True, True)
    
    print(result1)
    print(result2)
    print(result3)