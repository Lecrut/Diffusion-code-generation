def logic_and(a, b):
    return a and b
def logic_or(a, b):
    return a or b
def logic_not(a):
    return not a
def logic_xor(a, b):
    return a ^ b
if __name__ == '__main__':
    val1 = True
    val2 = False
    print(f"val1: {val1}")
    print(f"val2: {val2}")
    and_result = logic_and(val1, val2)
    print(f"AND result ({val1} AND {val2}): {and_result}")
    or_result = logic_or(val1, val2)
    print(f"OR result ({val1} OR {val2}): {or_result}")
    not_result = logic_not(val1)
    print(f"NOT result (NOT {val1}): {not_result}")
    xor_result = logic_xor(val1, val2)
    print(f"XOR result ({val1} XOR {val2}): {xor_result}")