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
    and_result = logic_and(val1, val2)
    or_result = logic_or(val1, val2)
    not_result = logic_not(val1)
    xor_result = logic_xor(val1, val2)
    print(f"AND({val1}, {val2}): {and_result}")
    print(f"OR({val1}, {val2}): {or_result}")
    print(f"NOT({val1}): {not_result}")
    print(f"XOR({val1}, {val2}): {xor_result}")