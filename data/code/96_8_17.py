def evaluate_expression(a, b, c, d):
    return a and b or (c and (not d))
if __name__ == '__main__':
    test_cases = [(True, True, False, True), (False, False, True, False), (True, False, True, True), (False, True, False, False)]
    for a, b, c, d in test_cases:
        result = evaluate_expression(a, b, c, d)
        print(f'evaluate_expression({a}, {b}, {c}, {d}) = {result}')