def generate_truth_table(expression):
    if not isinstance(expression, str):
        raise ValueError("Input must be a string representing a boolean expression.")

    variables = set()
    for char in expression:
        if char.isalpha():
            variables.add(char)
    
    num_variables = len(variables)
    if num_variables == 1:
        variable_name = list(variables)[0]
        truth_table = [{'a': True, 'result': eval(expression.replace('a', str(True)))}, {'a': False, 'result': eval(expression.replace('a', str(False)))}]
    elif num_variables == 2:
        truth_table = []
        for a in [True, False]:
            for b in [True, False]:
                result = eval(expression.replace('a', str(a)).replace('b', str(b)))
                truth_table.append({'a': a, 'b': b, 'result': result})
    else:
        raise ValueError("Expression must involve exactly one or two boolean variables.")

    return truth_table

if __name__ == '__main__':
    sample_expression = "a and not b"
    print(generate_truth_table(sample_expression))