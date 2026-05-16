def logical_and(a, b):
    return a and b
def logical_or(a, b):
    return a or b
def logical_not(a):
    return not a
def logical_xor(a, b):
    return a ^ b
if __name__ == '__main__':
    val1 = True
    val2 = False
    and_result = logical_and(val1, val2)
    or_result = logical_or(val1, val2)
    not_result = logical_not(val1)
    xor_result = logical_xor(val1, val2)
    print(f"val1: {val1}")
    print(f"val2: {val2}")
    print(f"AND result: {and_result}")
    print(f"OR result: {or_result}")
    print(f"NOT result: {not_result}")
    print(f"XOR result: {xor_result}")