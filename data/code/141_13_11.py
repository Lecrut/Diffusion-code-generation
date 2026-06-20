def validate_bitmask(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Bitmask must be a non-negative integer")

def and_gate(a, b):
    validate_bitmask(a)
    validate_bitmask(b)
    return a & b

def or_gate(a, b):
    validate_bitmask(a)
    validate_bitmask(b)
    return a | b

def not_gate(a):
    validate_bitmask(a)
    return ~a

if __name__ == '__main__':
    print("Testing AND gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"AND({bin(a_val)}, {bin(b_val)}) = {bin(and_gate(a_val, b_val))}")
    
    a_val = 0b1111
    b_val = 0b0000
    print(f"AND({bin(a_val)}, {bin(b_val)}) = {bin(and_gate(a_val, b_val))}")
    
    print("\nTesting OR gate:")
    a_val = 0b1100
    b_val = 0b1010
    print(f"OR({bin(a_val)}, {bin(b_val)}) = {bin(or_gate(a_val, b_val))}")
    
    a_val = 0b1111
    b_val = 0b0000
    print(f"OR({bin(a_val)}, {bin(b_val)}) = {bin(or_gate(a_val, b_val))}")
    
    print("\nTesting NOT gate:")
    a_val = 0b1100
    print(f"NOT({bin(a_val)}) = {bin(not_gate(a_val))}")