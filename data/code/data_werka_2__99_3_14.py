def evaluate_boolean_expression(a, b, c):
    result1 = (a > b) and (b < c) or (not a)
    result2 = (a == b) or (c > a) and (b != c)
    result3 = not ((a > b) and (b > c)) or (a < c)
    result4 = (a and b) or (c and not a)
    result5 = (a or b) and (c or not b)
    return result1, result2, result3, result4, result5

if __name__ == '__main__':
    a_val = 5
    b_val = 3
    c_val = 8
    results = evaluate_boolean_expression(a_val, b_val, c_val)
    print(results)