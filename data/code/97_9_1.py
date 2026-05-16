def truth_table(a, b):
    return {
        (a, b): (True, True),
        (a, not b): (True, False),
        (not a, b): (False, True),
        (not a, not b): (False, False)
    }
if __name__ == '__main__':
    a_val = True
    b_val = False
    result = truth_table(a_val, b_val)
    print(result)