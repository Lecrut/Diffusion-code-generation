def logic_and(a, b):
    return a & b
def logic_or(a, b):
    return a | b
def logic_not(a):
    return not a
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    print(f"AND({a_val}, {b_val}): {logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {logic_not(a_val)}")
    a_val = 1
    b_val = 1
    print(f"AND({a_val}, {b_val}): {logic_and(a_val, b_val)}")
    print(f"OR({a_val}, {b_val}): {logic_or(a_val, b_val)}")
    print(f"NOT({a_val}): {logic_not(a_val)}")