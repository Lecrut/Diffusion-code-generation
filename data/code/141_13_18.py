def and_gate(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return a & b

def or_gate(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    return a | b

def not_gate(a):
    if not isinstance(a, int):
        raise ValueError("Input must be an integer")
    return ~a & 1

if __name__ == '__main__':
    print("Testing AND gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"AND({bin(a_val)}, {bin(b_val)}) = {and_gate(a_val, b_val)}")
    
    print("\nTesting OR gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"OR({bin(a_val)}, {bin(b_val)}) = {or_gate(a_val, b_val)}")
    
    print("\nTesting NOT gate:")
    a_val = 0b1100
    print(f"NOT({bin(a_val)}) = {not_gate(a_val)}")