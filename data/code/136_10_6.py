def logical_operators_demo():
    a = True
    b = False

    and_result = a and b
    or_result = a or b
    not_a_result = not a
    xor_result = (a and not b) or (not a and b)

    return and_result, or_result, not_a_result, xor_result

if __name__ == '__main__':
    and_result, or_result, not_a_result, xor_result = logical_operators_demo()
    print(f"a AND b: {and_result}")
    print(f"a OR b: {or_result}")
    print(f"NOT a: {not_a_result}")
    print(f"a XOR b: {xor_result}")