def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
if __name__ == '__main__':
    print("Testing AND gate:")
    a_val = True
    b_val = False
    print(f"AND({a_val}, {b_val}) = {and_gate(a_val, b_val)}")
    a_val = True
    b_val = True
    print(f"AND({a_val}, {b_val}) = {and_gate(a_val, b_val)}")
    print("\nTesting OR gate:")
    a_val = True
    b_val = False
    print(f"OR({a_val}, {b_val}) = {or_gate(a_val, b_val)}")
    a_val = False
    b_val = False
    print(f"OR({a_val}, {b_val}) = {or_gate(a_val, b_val)}")
    print("\nTesting NOT gate:")
    a_val = True
    print(f"NOT({a_val}) = {not_gate(a_val)}")
    a_val = False
    print(f"NOT({a_val}) = {not_gate(a_val)}")
    print("\nTesting combined operations:")
    x = True
    y = True
    print(f"NOT(AND({x}, {y})) = {not_gate(and_gate(x, y))}")
    print(f"OR(NOT({x}), {y}) = {or_gate(not_gate(x), y)}")