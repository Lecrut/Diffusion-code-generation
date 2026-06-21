def evaluate_boolean_expression():
    truth_table = []
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                result = (a & b) | (~c)
                truth_table.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return truth_table

if __name__ == '__main__':
    print(evaluate_boolean_expression())