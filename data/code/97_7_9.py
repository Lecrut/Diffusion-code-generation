def generate_truth_table(variables):
    variable_count = len(variables)
    header = " | ".join([f"{var} |" for var in variables]) + " Result\n"
    separator = "-" * (len(header) - 1) + "\n"
    
    print(separator)
    print(header)
    print(separator)
    
    row_format = f"{' | '.join(['{}'] * variable_count)} | {{}}"
    for combination in product([True, False], repeat=variable_count):
        result = eval_truth_expression(variables, combination)
        print(row_format.format(*combination, result))

def eval_truth_expression(variables, values):
    expression = " and ".join(f"{vars} == {vals}" for vars, vals in zip(variables, values))
    return eval(expression)

if __name__ == '__main__':
    sample_variables = ['P', 'Q', 'R']
    sample_data = list(product([True, False], repeat=len(sample_variables)))
    
    generate_truth_table(sample_variables)