def logic_and(a, b):
    return a & b
def logic_or(a, b):
    return a | b
def logic_not(a):
    return ~a
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    print("--- AND Operation ---")
    result_and = logic_and(a_val, b_val)
    print(f"AND({a_val}, {b_val}) = {result_and}")
    a_val = 1
    b_val = 1
    print("\n--- OR Operation ---")
    result_or = logic_or(a_val, b_val)
    print(f"OR({a_val}, {b_val}) = {result_or}")
    a_val = 0
    b_val = 0
    print("\n--- NOT Operation ---")
    result_not = logic_not(a_val)
    print(f"NOT({a_val}) = {result_not}")