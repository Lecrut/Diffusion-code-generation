def evaluate_expression(variables):
    result = (variables['A'] and variables['B']) or (variables['C'] and not variables['D'])
    return result

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    variables_dict = dict(sample_values)
    print(evaluate_expression(variables_dict))