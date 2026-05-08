def bitwise_logic(a, b):
    and_result = a & b
    or_result = a | b
    not_a_result = ~a
    not_b_result = ~b
    return and_result, or_result, not_a_result, not_b_result
if __name__ == '__main__':
    a = 5
    b = 3
    and_res, or_res, not_a_res, not_b_res = bitwise_logic(a, b)
    print(f"A: {a} ({bin(a)})")
    print(f"B: {b} ({bin(b)})")
    print(f"A AND B: {and_res} ({bin(and_res)})")
    print(f"A OR B: {or_res} ({bin(or_res)})")
    print(f"NOT A: {not_a_res} ({bin(not_a_res)})")
    print(f"NOT B: {not_b_res} ({bin(not_b_res)})")