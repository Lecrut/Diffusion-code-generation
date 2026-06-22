def evaluate_nested_logic(a, b, c, d):
    left = a and b
    right = c and (not d)
    return left or right

if __name__ == '__main__':
    res = evaluate_nested_logic(True, False, True, False)
    print(res)
    res2 = evaluate_nested_logic(False, True, False, True)
    print(res2)
    res3 = evaluate_nested_logic(True, True, False, True)
    print(res3)
    res4 = evaluate_nested_logic(False, False, True, False)
    print(res4)