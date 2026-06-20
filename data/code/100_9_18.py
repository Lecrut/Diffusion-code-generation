import re

def is_valid_boolean_expression(expression):
    pattern = '^\\s*(True|False)\\s*$'
    return bool(re.match(pattern, expression))
if __name__ == '__main__':
    sample_values = ['True', 'False', 'true', 'false', '1', '0', 'hello', '']
    for value in sample_values:
        print(f"'{value}': {is_valid_boolean_expression(value)}")