def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
    operations = {"==": lambda x, y: x == y}
    operation_key = "=="
    result = operations[operation_key](a, b)
    return result, operation_key

if __name__ == '__main__':
    bool1 = True
    bool2 = True
    result1, op1 = compare_booleans(bool1, bool2)
    print(f"Comparing {bool1} and {bool2}: Result={result1}, Operation={op1}")
    
    bool3 = False
    bool4 = True
    result2, op2 = compare_booleans(bool3, bool4)
    print(f"Comparing {bool3} and {bool4}: Result={result2}, Operation={op2}")
    
    bool5 = True
    bool6 = False
    result3, op3 = compare_booleans(bool5, bool6)
    print(f"Comparing {bool5} and {bool6}: Result={result3}, Operation={op3}")