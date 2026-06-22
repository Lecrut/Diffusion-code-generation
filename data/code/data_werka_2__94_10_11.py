def _validate_boolean(val, name):
    if not isinstance(val, bool):
        raise ValueError(f"{name} must be a boolean")

def _validate_boolean_list(lst, name):
    if not isinstance(lst, list):
        raise ValueError(f"{name} must be a list")
    for i, item in enumerate(lst):
        if not isinstance(item, bool):
            raise ValueError(f"Item at index {i} in {name} must be a boolean")

def is_any_true(value, values):
    _validate_boolean(value, "value")
    _validate_boolean_list(values, "values")
    
    if value:
        return True
    
    for v in values:
        if v:
            return True
            
    return False

if __name__ == '__main__':
    result1 = is_any_true(True, [False, False])
    print(result1)
    
    result2 = is_any_true(False, [False, True])
    print(result2)
    
    result3 = is_any_true(False, [False, False])
    print(result3)