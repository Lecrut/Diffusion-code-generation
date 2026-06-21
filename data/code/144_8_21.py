def evaluate_expression(variables):
    A, B, C, D = map(int, variables)
    result = (A or B) and (C or D)
    return result

if __name__ == '__main__':
    variable_combinations = {
        '0000': False,
        '0001': True,
        '0010': True,
        '0011': True,
        '0100': True,
        '0101': True,
        '0110': True,
        '0111': True,
        '1000': True,
        '1001': True,
        '1010': True,
        '1011': True,
        '1100': True,
        '1101': True,
        '1110': True,
        '1111': True
    }

    for variables, expected in variable_combinations.items():
        result = evaluate_expression(variables)
        print(f"{variables}: {result} (Expected: {expected})")