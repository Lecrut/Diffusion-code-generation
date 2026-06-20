class BooleanComparator:
    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    
    result1 = comparator.compare(True, True)
    print(f"Comparing True and True: {result1}")
    
    result2 = comparator.compare(False, False)
    print(f"Comparing False and False: {result2}")
    
    result3 = comparator.compare(True, False)
    print(f"Comparing True and False: {result3}")
    
    result4 = comparator.compare(False, True)
    print(f"Comparing False and True: {result4}")