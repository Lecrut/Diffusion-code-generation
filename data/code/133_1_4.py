def evaluate_statements(statements):
    results = {}
    for statement in statements:
        try:
            result = eval(statement)
            if not isinstance(result, bool):
                raise ValueError(f"Statement '{statement}' did not evaluate to a boolean value.")
            results[statement] = result
        except Exception as e:
            print(f"Error evaluating statement '{statement}': {e}")
    return results

if __name__ == '__main__':
    sample_statements = [
        "1 + 1 == 2",
        "3 > 5",
        "'hello' == 'hello'",
        "not True",
        "x = 10; x < 20"
    ]
    print(evaluate_statements(sample_statements))