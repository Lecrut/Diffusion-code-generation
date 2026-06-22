def check_or_condition(a, b):
    if not isinstance(a, bool):
        raise ValueError("Argument a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("Argument b must be a boolean")
    
    val_a = 1 if a else 0
    val_b = 1 if b else 0
    
    return bool(val_a | val_b)

if __name__ == '__main__':
    res = check_or_condition(False, True)
    print(res)