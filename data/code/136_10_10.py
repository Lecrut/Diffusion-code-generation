def logical_operators_demo():
    x = True
    y = False
    z = True

    and_result = x and y
    or_result = x or y
    not_x_result = not x
    xor_result = (x and not y) or (not x and y)

    return and_result, or_result, not_x_result, xor_result

if __name__ == '__main__':
    and_res, or_res, not_and_res, xor_res = logical_operators_demo()
    print("x AND y:", and_res)
    print("x OR y:", or_res)
    print("NOT x:", not_and_res)
    print("x XOR y:", xor_res)