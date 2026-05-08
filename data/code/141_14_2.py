def bitwise_logic(a, b):
    and_result = a & b
    or_result = a | b
    not_a = ~a
    not_b = ~b
    return and_result, or_result, not_a, not_b
if __name__ == '__main__':
    a = 5
    b = 3
    and_res, or_res, not_a, not_b = bitwise_logic(a, b)
    print(f"A: {a} ({bin(a)})")
    print(f"B: {b} ({bin(b)})")
    print(f"A AND B: {and_res} ({bin(and_res)})")
    print(f"A OR B: {or_res} ({bin(or_res)})")
    print(f"NOT A: {not_a} ({bin(not_a)})")
    print(f"NOT B: {not_b} ({bin(not_b)})")