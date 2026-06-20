AND_OP = 'AND'
OR_OP = 'OR'
XOR_OP = 'XOR'

def truth_table(a, b):
    return [
        (a, b, AND_OP),
        (a, not b, OR_OP),
        (not a, b, XOR_OP),
        (not a, not b, AND_OP)
    ]

if __name__ == '__main__':
    sample_values = [True, False]
    for a in sample_values:
        for b in sample_values:
            table = truth_table(a, b)
            print(table)