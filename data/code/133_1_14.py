def evaluate_statements(statements):
    results = {}
    truth_values = {'True': True, 'False': False}
    for statement in statements:
        if statement in truth_values:
            results[statement] = truth_values[statement]
        else:
            try:
                result = eval(statement)
                results[statement] = bool(result)
            except Exception as e:
                results[statement] = None
    return results

if __name__ == '__main__':
    sample_statements = [
        "1 + 1 == 2",
        "3 > 5",
        "'hello' == 'world'",
        "not False",
        "len([1, 2, 3]) > 2"
    ]
    print(evaluate_statements(sample_statements))