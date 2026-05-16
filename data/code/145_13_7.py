def evaluate_nested_expressions(a, b, c, d, x, y):
    result = []
    for i in range(10):
        sub_result = []
        for j in range(5):
            if i % 2 == 0:
                if j % 3 == 0:
                    if a > 5 and b < 10:
                        sub_result.append(True)
                    else:
                        sub_result.append(False)
                else:
                    if c == 10:
                        sub_result.append(True)
                    else:
                        sub_result.append(False)
            else:
                if d > 0 and x < y:
                    sub_result.append(True)
                else:
                    sub_result.append(False)
        result.append(sub_result)
    return result
if __name__ == '__main__':
    A = 7
    B = 8
    C = 10
    D = 1
    X = 5
    Y = 12
    evaluation_results = evaluate_nested_expressions(A, B, C, D, X, Y)
    print(evaluation_results)