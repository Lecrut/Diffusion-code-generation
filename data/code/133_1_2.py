def evaluate_statements(statements):
    results = {}
    for statement in statements:
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