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
        "2 + 2 == 4",
        "3 * 3 != 9",
        "10 > 5 and 5 < 10",
        "not (True or False)",
        "x = 5"
    ]
    print(evaluate_statements(sample_statements))