def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")

def logical_and(a, b):
    validate_boolean(a)
    validate_boolean(b)
    return a and b

def logical_or(a, b):
    validate_boolean(a)
    validate_boolean(b)
    return a or b

def logical_not(a):
    validate_boolean(a)
    return not a

if __name__ == '__main__':
    a = True
    b = False
    
    result_and = logical_and(a, b)
    result_or = logical_or(a, b)
    result_not_a = logical_not(a)
    
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Logical AND ({a} and {b}): {result_and}")
    print(f"Logical OR ({a} or {b}): {result_or}")
    print(f"Logical NOT of {a}: {result_not_a}")