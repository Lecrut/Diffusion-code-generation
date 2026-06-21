def evaluate_expression(variables):
    A, B, C, D = variables
    return (A or B) and (C or D)

if __name__ == '__main__':
    sample_values = [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1),
                    (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1),
                    (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1),
                    (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
    for values in sample_values:
        result = evaluate_expression(values)
        print(f"A={values[0]}, B={values[1]}, C={values[2]}, D={values[3]} -> {result}")