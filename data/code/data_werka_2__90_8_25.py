def check_condition(*args):
    if not args:
        raise ValueError("At least one boolean argument is required")
    
    for val in args:
        if not isinstance(val, bool):
            raise TypeError("All arguments must be boolean values")
    
    return any(args)

if __name__ == '__main__':
    result = check_condition(True, False, False)
    print(result)