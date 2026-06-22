TRUE_VALUE = True
FALSE_VALUE = False

def evaluate_nested_logic(a, b, c, d):
    ab_result = a and b
    cd_result = c and (not d)
    return ab_result or cd_result

if __name__ == '__main__':
    a_in = TRUE_VALUE
    b_in = FALSE_VALUE
    c_in = TRUE_VALUE
    d_in = FALSE_VALUE
    output = evaluate_nested_logic(a_in, b_in, c_in, d_in)
    print(output)