def and_gate(a, b, c):
    return a and b and c

if __name__ == '__main__':
    print(and_gate(True, True, True))
    print(and_gate(False, True, True))
    print(and_gate(True, False, True))
    print(and_gate(True, True, False))
    print(and_gate(False, False, False))