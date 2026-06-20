def evaluate_complex_expression():
    x = 5
    y = 3
    z = 8
    result = x > y and z < y
    return result
if __name__ == '__main__':
    result = evaluate_complex_expression()
    print(result)