xor = lambda a, b: a ^ b
and_ = lambda a, b: a & b
or_ = lambda a, b: a | b

if __name__ == '__main__':
    a_val = 1
    b_val = 0
    print(f"XOR of {a_val} and {b_val} is: {xor(a_val, b_val)}")
    a_val = 10
    b_val = 5
    print(f"AND of {a_val} and {b_val} is: {and_(a_val, b_val)}")
    a_val = 11
    b_val = 11
    print(f"OR of {a_val} and {b_val} is: {or_(a_val, b_val)}")