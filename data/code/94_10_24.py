def is_any_true(value, values):
    if not isinstance(value, bool):
        raise ValueError("The primary value must be a boolean.")
    if not hasattr(values, '__iter__'):
        raise ValueError("The values argument must be iterable.")
    
    def validate_bool_items(items):
        for item in items:
            if not isinstance(item, bool):
                raise ValueError("All items in the list must be booleans.")
    
    validate_bool_items(values)
    
    return value or any(values)

if __name__ == '__main__':
    result1 = is_any_true(True, [False, False, False])
    print(result1)
    
    result2 = is_any_true(False, [False, False, True])
    print(result2)
    
    result3 = is_any_true(False, [False, False, False])
    print(result3)