def evaluate_expression(variables):
    A = next(var[1] for var in variables if var[0] == 'A')
    B = next(var[1] for var in variables if var[0] == 'B')
    C = next(var[1] for var in variables if var[0] == 'C')
    D = next(var[1] for var in variables if var[0] == 'D')
    return (A and B) or (C and not D)

if __name__ == '__main__':
    sample_values = [('A', True), ('B', False), ('C', True), ('D', False)]
    print(evaluate_expression(sample_values))