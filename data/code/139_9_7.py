def logic_and(a, b):
    return a & b
def logic_or(a, b):
    return a | b
def logic_not(a):
    return ~a
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    and_result = logic_and(a_val, b_val)
    or_result = logic_or(a_val, b_val)
    not_result = logic_not(a_val)
    print(f"AND({a_val}, {b_val}): {and_result}")
    print(f"OR({a_val}, {b_val}): {or_result}")
    print(f"NOT({a_val}): {not_result}")