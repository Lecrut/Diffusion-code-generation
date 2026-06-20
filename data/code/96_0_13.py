def evaluate_nested_logic(a, b, c, d):
    ab = a and b
    cd_not_d = c and not d
    result = ab or cd_not_d
    return result

if __name__ == '__main__':
    A = False
    B = True
    C = False
    D = True
    result = evaluate_nested_logic(A, B, C, D)
    print(result)