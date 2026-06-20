def and_gate(a, b):
    return a * b

def or_gate(a, b):
    return a + b - a * b

def not_gate(a):
    return 1 - a
if __name__ == '__main__':
    print(and_gate(1, 1))
    print(or_gate(0, 1))
    print(not_gate(0))