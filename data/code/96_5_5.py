def evaluate_expression(variables):
    A = variables[0][1]
    B = variables[1][1]
    C = variables[2][1]
    D = variables[3][1]
    return (A and B) or (C and not D)

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', True)]
    result = evaluate_expression(sample_values)
    print(result)