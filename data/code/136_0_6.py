def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

if __name__ == '__main__':
    bool_values = {True: 'true', False: 'false'}
    
    a = True
    b = False
    
    result_and = logical_and(a, b)
    result_or = logical_or(a, b)
    result_not_a = logical_not(a)
    
    print(f"a = {bool_values[a]}")
    print(f"b = {bool_values[b]}")
    print(f"Logical AND ({a}, {b}): {result_and}")
    print(f"Logical OR ({a}, {b}): {result_or}")
    print(f"Logical NOT ({a}): {result_not_a}")