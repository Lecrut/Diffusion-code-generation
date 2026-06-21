def evaluate_boolean_expression():
    truth_table = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                result = (a & b) | (~c)
                truth_table.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return truth_table

if __name__ == '__main__':
    table = evaluate_boolean_expression()
    print(table)