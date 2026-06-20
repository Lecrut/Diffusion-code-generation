import ast

def evaluate_boolean_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        print(f'Syntax error: {e}')
        return None
if __name__ == '__main__':
    result = evaluate_boolean_expression('3 > 2 and 5 < 10')
    print(result)