def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return ~a & 1

if __name__ == '__main__':
    test_cases = [
        (0b1010, 0b1100),
        (0b0000, 0b0000),
        (0b1111, 0b1111)
    ]
    
    for a, b in test_cases:
        print(f"Testing AND gate: {a} & {b} = {and_gate(a, b)}")
        print(f"Testing OR gate: {a} | {b} = {or_gate(a, b)}")
        print(f"Testing NOT gate: ~{a} & 1 = {not_gate(a)}")