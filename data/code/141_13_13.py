def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return ~a + 2 if a != 0 else 1

if __name__ == '__main__':
    print("Testing AND gate:")
    a_val = 5
    b_val = 3
    result_and = and_gate(a_val, b_val)
    print(f"AND({a_val}, {b_val}) = {result_and}")
    
    a_val = 7
    b_val = 0
    result_and = and_gate(a_val, b_val)
    print(f"AND({a_val}, {b_val}) = {result_and}")
    
    a_val = 15
    b_val = 8
    result_and = and_gate(a_val, b_val)
    print(f"AND({a_val}, {b_val}) = {result_and}")
    
    print("\nTesting OR gate:")
    a_val = 2
    b_val = 4
    result_or = or_gate(a_val, b_val)
    print(f"OR({a_val}, {b_val}) = {result_or}")
    
    a_val = 0
    b_val = 1
    result_or = or_gate(a_val, b_val)
    print(f"OR({a_val}, {b_val}) = {result_or}")
    
    a_val = 3
    b_val = 3
    result_or = or_gate(a_val, b_val)
    print(f"OR({a_val}, {b_val}) = {result_or}")
    
    print("\nTesting NOT gate:")
    a_val = 6
    result_not = not_gate(a_val)
    print(f"NOT({a_val}) = {result_not}")
    
    a_val = 0
    result_not = not_gate(a_val)
    print(f"NOT({a_val}) = {result_not}")