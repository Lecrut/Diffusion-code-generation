def logical_and(a: bool, b: bool) -> bool:
    return a and b

def logical_or(a: bool, b: bool) -> bool:
    return a or b

def logical_not(a: bool) -> bool:
    return not a

if __name__ == '__main__':
    a = True
    b = False
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Logical AND ({a}, {b}): {logical_and(a, b)}")
    print(f"Logical OR ({a}, {b}): {logical_or(a, b)}")
    print(f"Logical NOT ({a}): {logical_not(a)}")