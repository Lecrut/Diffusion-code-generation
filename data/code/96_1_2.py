def evaluate_nested_logic(a, b, c, d):
    intermediate_result_1 = a and b
    intermediate_result_2 = c and not d
    final_result = intermediate_result_1 or intermediate_result_2
    return final_result
if __name__ == '__main__':
    a_val = True
    b_val = False
    c_val = True
    d_val = False
    result = evaluate_nested_logic(a_val, b_val, c_val, d_val)
    print(result)