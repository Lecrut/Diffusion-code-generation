and_gate = lambda a, b: a & b
or_gate = lambda a, b: a | b
not_gate = lambda a: ~a + 2
xor_gate = lambda a, b: a ^ b
if __name__ == '__main__':
    print(and_gate(1, 0))
    print(or_gate(1, 0))
    print(not_gate(1))
    print(xor_gate(1, 0))