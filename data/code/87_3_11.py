def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    value1 = True
    value2 = False
    value3 = True
    result = evaluate_expression(value1, value2, value3)
    print(result)