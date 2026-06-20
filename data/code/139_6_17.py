def and_gate(a, b):
    if not (isinstance(a, int) or isinstance(a, str)) or not (isinstance(b, int) or isinstance(b, str)):
        raise TypeError("Inputs must be integers or binary strings.")
    
    a_val = int(a, 2) if isinstance(a, str) else a
    b_val = int(b, 2) if isinstance(b, str) else b
    
    return a_val & b_val

def or_gate(a, b):
    if not (isinstance(a, int) or isinstance(a, str)) or not (isinstance(b, int) or isinstance(b, str)):
        raise TypeError("Inputs must be integers or binary strings.")
    
    a_val = int(a, 2) if isinstance(a, str) else a
    b_val = int(b, 2) if isinstance(b, str) else b
    
    return a_val | b_val

def not_gate(a):
    if not (isinstance(a, int) or isinstance(a, str)):
        raise TypeError("Input must be an integer or binary string.")
    
    a_val = int(a, 2) if isinstance(a, str) else a
    
    return ~a_val & 1

def xor_gate(a, b):
    if not (isinstance(a, int) or isinstance(a, str)) or not (isinstance(b, int) or isinstance(b, str)):
        raise TypeError("Inputs must be integers or binary strings.")
    
    a_val = int(a, 2) if isinstance(a, str) else a
    b_val = int(b, 2) if isinstance(b, str) else b
    
    return a_val ^ b_val

if __name__ == '__main__':
    print(and_gate("101", "110"))
    print(and_gate(1, 0))
    print(and_gate("1", "0"))
    try:
        print(and_gate("101", "invalid"))
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        print(and_gate(5, "2"))
    except TypeError as e:
        print(f"Error caught: {e}")

    print(or_gate("101", "110"))
    print(or_gate(1, 0))
    print(or_gate("1", "0"))
    try:
        print(or_gate("101", "invalid"))
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        print(or_gate(5, "2"))
    except TypeError as e:
        print(f"Error caught: {e}")

    print(not_gate("101"))
    print(not_gate(1))
    print(not_gate("1"))
    try:
        print(not_gate("invalid"))
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        print(not_gate(5.5))
    except TypeError as e:
        print(f"Error caught: {e}")

    print(xor_gate("101", "110"))
    print(xor_gate(1, 0))
    print(xor_gate("1", "0"))
    try:
        print(xor_gate("101", "invalid"))
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        print(xor_gate(5, "2"))
    except TypeError as e:
        print(f"Error caught: {e}")