def truth_table(a, b):
    and_result = (a and b)
    or_result = (a or b)
    xor_result = (a != b)
    return [(a, b), (a, not b), (not a, b), (not a, not b)], [and_result, or_result, xor_result]

if __name__ == '__main__':
    a_val = False
    b_val = True
    table, results = truth_table(a_val, b_val)
    print("Truth Table:", table)
    print("Bitwise AND, OR, XOR Results:", results)