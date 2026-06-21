def negate(value):
    table = {True: False, False: True}
    if value not in table:
        raise ValueError("Input must be a boolean")
    return table[value]

if __name__ == '__main__':
    true_val = True
    false_val = False
    result1 = negate(true_val)
    result2 = negate(false_val)
    print(result1)
    print(result2)