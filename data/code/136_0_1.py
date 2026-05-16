def logical_and(a, b):
    return a & b
def logical_or(a, b):
    return a | b
def logical_not(a):
    return ~a
if __name__ == '__main__':
    a = 5
    b = 3
    result_and = logical_and(a, b)
    result_or = logical_or(a, b)
    result_not = logical_not(a)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Logical AND of {a} and {b}: {result_and}")
    print(f"Logical OR of {a} and {b}: {result_or}")
    print(f"Logical NOT of {a}: {result_not}")