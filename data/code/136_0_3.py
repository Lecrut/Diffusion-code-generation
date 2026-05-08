def logical_and(a, b):
    return a & b
def logical_or(a, b):
    return a | b
def logical_not(a):
    return ~a
if __name__ == '__main__':
    x = 5
    y = 3
    result_and = logical_and(x, y)
    result_or = logical_or(x, y)
    result_not = logical_not(x)
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Logical AND ({x}, {y}): {result_and}")
    print(f"Logical OR ({x}, {y}): {result_or}")
    print(f"Logical NOT ({x}): {result_not}")