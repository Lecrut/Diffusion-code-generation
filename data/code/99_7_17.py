import ast

def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except SyntaxError as e:
        print(f'Syntax error: {e}')
        return None
if __name__ == '__main__':
    sample_expression = '3 > 2 and not False'
    result = evaluate_boolean_expression(sample_expression)
    print(result)