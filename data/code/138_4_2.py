def truth_table(a, b):
    result = [
        (a, b),
        (a, not b),
        (not a, b),
        (not a, not b)
    ]
    return tuple(result)
if __name__ == '__main__':
    a_val = True
    b_val = True
    table = truth_table(a_val, b_val)
    print(table)