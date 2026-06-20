def truth_table(a, b):
    result = [
        (a, b),
        (a, not b),
        (not a, b),
        (not a, not b)
    ]
    return tuple(result)

def bitwise_operations(table):
    and_results = [(x[0] and x[1]) for x in table]
    or_results = [(x[0] or x[1]) for x in table]
    xor_results = [((x[0] and not x[1]) or (not x[0] and x[1])) for x in table]
    return and_results, or_results, xor_results

if __name__ == '__main__':
    a_val = True
    b_val = False
    table = truth_table(a_val, b_val)
    and_res, or_res, xor_res = bitwise_operations(table)
    print("Truth Table:", table)
    print("Bitwise AND:", and_res)
    print("Bitwise OR:", or_res)
    print("Bitwise XOR:", xor_res)