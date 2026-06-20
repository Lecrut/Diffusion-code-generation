xor_gate = lambda a, b: a ^ b
and_gate = lambda a, b: a & b
or_gate = lambda a, b: a | b

if __name__ == '__main__':
    a_val = 3
    b_val = 5
    xor_result = xor_gate(a_val, b_val)
    print(f"XOR of {a_val} and {b_val} is: {xor_result}")
    
    a_val = 7
    b_val = 10
    and_result = and_gate(a_val, b_val)
    print(f"AND of {a_val} and {b_val} is: {and_result}")
    
    a_val = 2
    b_val = 4
    or_result = or_gate(a_val, b_val)
    print(f"OR of {a_val} and {b_val} is: {or_result}")