def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    condition_a = True
    condition_b = False
    condition_c = True
    result = evaluate_expression(condition_a, condition_b, condition_c)
    print(result)