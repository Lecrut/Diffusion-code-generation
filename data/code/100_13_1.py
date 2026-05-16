def logic_checker(a, b):
    and_result = a and b
    or_result = a or b
    not_a_result = not a
    not_b_result = not b
    return and_result, or_result, not_a_result, not_b_result
if __name__ == '__main__':
    input_a = True
    input_b = False
    and_res, or_res, not_a_res, not_b_res = logic_checker(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"AND result: {and_res}")
    print(f"OR result: {or_res}")
    print(f"NOT A result: {not_a_res}")
    print(f"NOT B result: {not_b_res}")