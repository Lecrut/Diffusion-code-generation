import re

def is_valid_boolean_expression(expression):
    pattern = '^\\s*(True|False)\\s*$'
    return bool(re.match(pattern, expression))
if __name__ == '__main__':
    test_cases = ['True', 'False', 'true', 'false', '1', '0', '', '   True   ', '  False  ']
    for case in test_cases:
        print(f"'{case}': {is_valid_boolean_expression(case)}")