xor_gate = lambda a, b: a ^ b
and_gate = lambda a, b: a & b
or_gate = lambda a, b: a | b

if __name__ == '__main__':
    a_val = 1
    b_val = 0
    result_xor = xor_gate(a_val, b_val)
    print(f"XOR of {a_val} and {b_val} is: {result_xor}")
    
    a_val = 3
    b_val = 5
    result_and = and_gate(a_val, b_val)
    print(f"AND of {a_val} and {b_val} is: {result_and}")
    
    a_val = 2
    b_val = 4
    result_or = or_gate(a_val, b_val)
    print(f"OR of {a_val} and {b_val} is: {result_or}")