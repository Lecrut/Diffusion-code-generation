def truth_table(a, b):
    results = {}
    results[(a, b)] = True
    results[(a, not b)] = True
    results[(not a, b)] = True
    results[(not a, not b)] = True
    return results
if __name__ == '__main__':
    a_val = True
    b_val = False
    table = truth_table(a_val, b_val)
    print(table)