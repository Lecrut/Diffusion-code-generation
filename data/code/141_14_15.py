AND_GATE = lambda a, b: a & b
OR_GATE = lambda a, b: a | b
NOT_GATE = lambda a: ~a

if __name__ == '__main__':
    a = 5
    b = 3
    and_res = AND_GATE(a, b)
    or_res = OR_GATE(a, b)
    not_a = NOT_GATE(a)
    not_b = NOT_GATE(b)
    print(f"A: {a} ({bin(a)})")
    print(f"B: {b} ({bin(b)})")
    print(f"A AND B: {and_res} ({bin(and_res)})")
    print(f"A OR B: {or_res} ({bin(or_res)})")
    print(f"NOT A: {not_a} ({bin(not_a)})")
    print(f"NOT B: {not_b} ({bin(not_b)})")