def evaluate_statements(statements):
    results = {}
    for statement in statements:
        try:
            result = eval(statement)
            if isinstance(result, bool):
                results[statement] = result
            else:
                raise ValueError(f"Statement '{statement}' does not evaluate to a boolean value.")
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