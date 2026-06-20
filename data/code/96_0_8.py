def evaluate_nested_logic(a, b, c, d):
    inner_and_1 = a and b
    inner_and_2 = c and not d
    result = inner_and_1 or inner_and_2
    return result

if __name__ == '__main__':
    A = False
    B = True
    C = False
    D = True
    logic_result = evaluate_nested_logic(A, B, C, D)
    print(logic_result)