class BooleanComparator:
    def compare(self, a: bool, b: bool) -> tuple[bool, str]:
        result = a == b
        operation = "=="
        return result, operation

if __name__ == '__main__':
    comparator = BooleanComparator()
    
    bool1 = True
    bool2 = True
    result1, op1 = comparator.compare(bool1, bool2)
    print(f"Comparing {bool1} and {bool2}: Result={result1}, Operation={op1}")
    
    bool3 = False
    bool4 = True
    result2, op2 = comparator.compare(bool3, bool4)
    print(f"Comparing {bool3} and {bool4}: Result={result2}, Operation={op2}")
    
    bool5 = True
    bool6 = False
    result3, op3 = comparator.compare(bool5, bool6)
    print(f"Comparing {bool5} and {bool6}: Result={result3}, Operation={op3}")