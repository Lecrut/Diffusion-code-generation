def logic_checker(a, b):
    and_result = a and b
    or_result = a or b
    not_a_result = not a
    not_b_result = not b
    return and_result, or_result, not_a_result, not_b_result
if __name__ == '__main__':
    var1 = True
    var2 = False
    and_res, or_res, not_var1, not_var2 = logic_checker(var1, var2)
    print(f"Input A: {var1}, Input B: {var2}")
    print(f"AND result: {and_res}")
    print(f"OR result: {or_res}")
    print(f"NOT A result: {not_var1}")
    print(f"NOT B result: {not_var2}")