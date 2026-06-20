def evaluate_statements(statements):
    results = {}
    for statement in statements:
        try:
            results[statement] = eval(statement)
        except Exception as e:
            results[statement] = str(e)
    return results

if __name__ == '__main__':
    sample_statements = [
        '1 + 1 == 2',
        '3 > 5',
        '"hello" == "world"',
        'x = 5; x == 5'
    ]
    print(evaluate_statements(sample_statements))