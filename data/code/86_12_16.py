def compare_booleans(a: bool, b: bool) -> str:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    
    return "Equal" if a == b else "Not Equal"

if __name__ == '__main__':
    try:
        result1 = compare_booleans(True, True)
        print(result1)
        
        result2 = compare_booleans(True, False)
        print(result2)
        
        result3 = compare_booleans(False, True)
        print(result3)
        
        result4 = compare_booleans(False, False)
        print(result4)
    except ValueError as e:
        print(e)