def is_any_true(value, values):
    if not isinstance(value, bool):
        raise ValueError("First argument must be a boolean")
    if not isinstance(values, (list, tuple)):
        raise ValueError("Second argument must be a list or tuple")
    
    for item in values:
        if not isinstance(item, bool):
            raise ValueError("All elements in the list must be booleans")
            
    if value:
        return True
        
    for v in values:
        if v:
            return True
            
    return False

if __name__ == '__main__':
    result1 = is_any_true(True, [False, False])
    print(result1)
    
    result2 = is_any_true(False, [True, False])
    print(result2)
    
    result3 = is_any_true(False, [False, False])
    print(result3)