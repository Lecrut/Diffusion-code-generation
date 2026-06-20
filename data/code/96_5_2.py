def evaluate_expression(variables):
    A, B = variables[0]
    C, D = variables[2]
    return (A and B) or (C and not D)

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    result = evaluate_expression(sample_values)
    print(result)