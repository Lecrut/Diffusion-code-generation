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
    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b} (binary: {bin(b)})")
    print(f"AND result (a & b): {and_res} (binary: {bin(and_res)})")
    print(f"OR result (a | b): {or_res} (binary: {bin(or_res)})")
    print(f"NOT a (~a): {not_a} (binary: {bin(not_a)})")
    print(f"NOT b (~b): {not_b} (binary: {bin(not_b)})")