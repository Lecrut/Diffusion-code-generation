and_gate = lambda x, y: x & y
or_gate = lambda x, y: x | y
not_gate = lambda x: ~x + 2
xor_gate = lambda x, y: x ^ y
if __name__ == '__main__':
    print(and_gate(1, 0))
    print(or_gate(1, 0))
    print(not_gate(1))
    print(xor_gate(1, 0))