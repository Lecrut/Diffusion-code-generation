def evaluate_statements(statements):
    results = {}
    for statement in statements:
        try:
            result = eval(statement)
            if isinstance(result, bool):
                results[statement] = result
            else:
                raise ValueError(f"Statement '{statement}' does not evaluate to a boolean.")
        except Exception as e:
            print(f"Error evaluating statement '{statement}': {e}")
    return results

if __name__ == '__main__':
    sample_statements = [
        "1 + 1 == 2",
        "3 > 5",
        "'hello' == 'hello'",
        "True and False",
        "x = 10; x < 20"
    ]
    print(evaluate_statements(sample_statements))