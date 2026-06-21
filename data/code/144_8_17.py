def evaluate_expression(variables):
    A, B, C, D = map(int, variables)
    result = (A or B) and (C or D)
    return result

if __name__ == '__main__':
    truth_table = []
    for A in [0, 1]:
        for B in [0, 1]:
            for C in [0, 1]:
                for D in [0, 1]:
                    variables = f"{A}{B}{C}{D}"
                    result = evaluate_expression(variables)
                    truth_table.append((variables, result))
    print(truth_table)