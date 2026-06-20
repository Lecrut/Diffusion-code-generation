gates = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'NOT': lambda a: ~a,
    'XOR': lambda a, b: a ^ b
}

if __name__ == '__main__':
    a_val = 1
    b_val = 0
    print(f"AND of {a_val} and {b_val} is: {gates['AND'](a_val, b_val)}")
    print(f"OR of {a_val} and {b_val} is: {gates['OR'](a_val, b_val)}")
    print(f"NOT of {a_val} is: {gates['NOT'](a_val)}")
    print(f"XOR of {a_val} and {b_val} is: {gates['XOR'](a_val, b_val)}")

    a_val = 10
    b_val = 5
    print(f"AND of {a_val} and {b_val} is: {gates['AND'](a_val, b_val)}")
    print(f"OR of {a_val} and {b_val} is: {gates['OR'](a_val, b_val)}")
    print(f"NOT of {a_val} is: {gates['NOT'](a_val)}")
    print(f"XOR of {a_val} and {b_val} is: {gates['XOR'](a_val, b_val)}")

    a_val = 11
    b_val = 11
    print(f"AND of {a_val} and {b_val} is: {gates['AND'](a_val, b_val)}")
    print(f"OR of {a_val} and {b_val} is: {gates['OR'](a_val, b_val)}")
    print(f"NOT of {a_val} is: {gates['NOT'](a_val)}")
    print(f"XOR of {a_val} and {b_val} is: {gates['XOR'](a_val, b_val)}")