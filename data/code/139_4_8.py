if __name__ == '__main__':
    xor_gate = lambda a, b: a ^ b
    and_gate = lambda a, b: a & b
    or_gate = lambda a, b: a | b
    not_gate = lambda a: ~a

    print(xor_gate(1, 0))
    print(and_gate(10, 5))
    print(or_gate(11, 11))
    print(not_gate(4))