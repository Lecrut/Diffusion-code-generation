def evaluate_expression(expression):
    result = eval(expression)
    return result

if __name__ == '__main__':
    expression_str = '10 * (5 + 3) - 2 // 4'
    intermediate_result = evaluate_expression(expression_str)
    print(f"Intermediate Result: {intermediate_result}")