def bitwise_logic(a, b):
    and_result = a & b
    or_result = a | b
    not_a_result = not a
    not_b_result = not b
    return and_result, or_result, not_a_result, not_b_result
if __name__ == '__main__':
    a_val = 5
    b_val = 12
    and_res, or_res, not_a_res, not_b_res = bitwise_logic(a_val, b_val)
    print(f"a = {a_val} (binary: {bin(a_val)})")
    print(f"b = {b_val} (binary: {bin(b_val)})")
    print("-" * 20)
    print(f"AND (a & b): {and_res} (binary: {bin(and_res)})")
    print(f"OR (a | b): {or_res} (binary: {bin(or_res)})")
    print(f"NOT a (~a): {not_a_res} (binary: {bin(not_a_res)})")
    print(f"NOT b (~b): {not_b_res} (binary: {bin(not_b_res)})")