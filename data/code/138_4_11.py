AND_OP = 'AND'
OR_OP = 'OR'
XOR_OP = 'XOR'

def truth_table(a, b):
    results = [
        (a, b, AND_OP),
        (a, not b, AND_OP),
        (not a, b, AND_OP),
        (not a, not b, AND_OP),
        (a, b, OR_OP),
        (a, not b, OR_OP),
        (not a, b, OR_OP),
        (not a, not b, OR_OP),
        (a, b, XOR_OP),
        (a, not b, XOR_OP),
        (not a, b, XOR_OP),
        (not a, not b, XOR_OP)
    ]
    return results

if __name__ == '__main__':
    a_val = True
    b_val = False
    table = truth_table(a_val, b_val)
    for row in table:
        print(row)