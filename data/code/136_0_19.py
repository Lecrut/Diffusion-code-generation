def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

if __name__ == '__main__':
    x = True
    y = False
    result_and = logical_and(x, y)
    result_or = logical_or(x, y)
    result_not = logical_not(x)
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Logical AND ({x}, {y}): {result_and}")
    print(f"Logical OR ({x}, {y}): {result_or}")
    print(f"Logical NOT ({x}): {result_not}")