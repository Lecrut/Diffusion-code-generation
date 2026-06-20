def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

if __name__ == '__main__':
    a = True
    b = False
    result_and = logical_and(a, b)
    result_or = logical_or(a, b)
    result_not = logical_not(a)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Logical AND ({a} and {b}): {result_and}")
    print(f"Logical OR ({a} or {b}): {result_or}")
    print(f"Logical NOT ({a}): {result_not}")