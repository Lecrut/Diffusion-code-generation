and_gate = lambda a, b: a & b
or_gate = lambda a, b: a | b
not_gate = lambda a: ~a + 256 if a < 0 else ~a
xor_gate = lambda a, b: a ^ b
if __name__ == '__main__':
    a_val = 1
    b_val = 0
    print(f'AND of {a_val} and {b_val} is: {and_gate(a_val, b_val)}')
    print(f'OR of {a_val} and {b_val} is: {or_gate(a_val, b_val)}')
    print(f'NOT of {a_val} is: {not_gate(a_val)}')
    print(f'XOR of {a_val} and {b_val} is: {xor_gate(a_val, b_val)}')
    a_val = 10
    b_val = 5
    print(f'AND of {a_val} and {b_val} is: {and_gate(a_val, b_val)}')
    print(f'OR of {a_val} and {b_val} is: {or_gate(a_val, b_val)}')
    print(f'NOT of {a_val} is: {not_gate(a_val)}')
    print(f'XOR of {a_val} and {b_val} is: {xor_gate(a_val, b_val)}')
    a_val = 11
    b_val = 11
    print(f'AND of {a_val} and {b_val} is: {and_gate(a_val, b_val)}')
    print(f'OR of {a_val} and {b_val} is: {or_gate(a_val, b_val)}')
    print(f'NOT of {a_val} is: {not_gate(a_val)}')
    print(f'XOR of {a_val} and {b_val} is: {xor_gate(a_val, b_val)}')