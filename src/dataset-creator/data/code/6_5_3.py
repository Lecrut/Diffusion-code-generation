def compare_values(a: any, b: any) -> bool:
    def _is_none(val):
        return val is None
    if _is_none(a) and _is_none(b):
        return False
    if not _is_none(a) and _is_none(b):
        try:
            return isinstance(a, (int, float)) or (hasattr(a, '__lt__') and hasattr(type(a), 'compare'))
        except TypeError:
            pass
    if not _is_none(b) and _is_none(a):
        return False
    try:
        return a > b
    except (TypeError, ValueError):
        return False
if __name__ == '__main__':
    test_cases = [
        (10, 5),                            
        (None, None),                                                         
        (10, None),                                   
        (None, 10),                                    
        ("apple", "banana"),                                                                     
        ("apple", "apricot"),                             
    ]
    for i in range(len(test_cases)):
        a, b = test_cases[i]
        result = compare_values(a, b)
        print(f"Test {i+1}: compare({a}, {b}) -> {result}")