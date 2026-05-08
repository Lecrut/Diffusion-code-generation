def logic_and(a, b):
    return a & b
def logic_or(a, b):
    return a | b
def logic_not(a):
    return ~a
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    result_and = logic_and(a_val, b_val)
    result_or = logic_or(a_val, b_val)
    result_not = logic_not(a_val)
    print(f"AND({a_val}, {b_val}): {result_and}")
    print(f"OR({a_val}, {b_val}): {result_or}")
    print(f"NOT({a_val}): {result_not}")