def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return ~a + 1

if __name__ == '__main__':
    print('Testing AND gate:')
    a_val = 12
    b_val = 10
    print(f'AND({a_val:b}, {b_val:b}) = {and_gate(a_val, b_val):b}')
    
    print('\nTesting OR gate:')
    a_val = 12
    b_val = 10
    print(f'OR({a_val:b}, {b_val:b}) = {or_gate(a_val, b_val):b}')
    
    print('\nTesting NOT gate:')
    a_val = 12
    print(f'NOT({a_val:b}) = {not_gate(a_val):b}')