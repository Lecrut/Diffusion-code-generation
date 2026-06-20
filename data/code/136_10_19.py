def logical_operators_demo():
    x = True
    y = False
    z = True

    and_result = x and y and z
    or_result = x or y or z
    not_x_result = not x
    not_y_result = not y

    return and_result, or_result, not_x_result, not_y_result

if __name__ == '__main__':
    and_res, or_res, not_x_res, not_y_res = logical_operators_demo()
    print(f"a AND b AND c: {and_res}")
    print(f"a OR b OR c: {or_res}")
    print(f"NOT a: {not_x_res}")
    print(f"NOT b: {not_y_res}")