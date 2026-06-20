import re

def evaluate_nested_expression(expression: str) -> bool:

    def clean_and_validate(expression):
        expression = re.sub('\\s+', '', expression)
        if not re.match('^\\(\\w+\\)$|^\\w+$', expression):
            raise ValueError('Invalid syntax for logical expression')
        return expression

    def evaluate(expression):
        if expression[0] == '(':
            inner_expression = expression[1:-1]
            if ',' in inner_expression:
                parts = inner_expression.split(',')
                return all((evaluate(part) for part in parts))
            else:
                raise ValueError('Invalid syntax inside parentheses')
        else:
            return expression.lower() == 'true'
    try:
        cleaned_expression = clean_and_validate(expression)
        return evaluate(cleaned_expression)
    except ValueError as e:
        print(f'Error: {e}')
        return False
if __name__ == '__main__':
    sample_value_1 = '(True, False, True)'
    sample_value_2 = 'False'
    print(evaluate_nested_expression(sample_value_1))
    print(evaluate_nested_expression(sample_value_2))