def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        print(f'Error evaluating expression: {e}')
        return None
if __name__ == '__main__':
    sample_expression = '3 > 2 and not False'
    result = evaluate_boolean_expression(sample_expression)
    print(result)