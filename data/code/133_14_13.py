def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        if " is True" in statement:
            results[statement] = True
        elif " is False" in statement:
            results[statement] = False
        else:
            raise ValueError(f"Invalid statement: {statement}")
    return results

if __name__ == '__main__':
    sample_statements = [
        "1 + 1 is True",
        "2 * 2 is False",
        "3 - 1 is True"
    ]
    print(evaluate_tf_statements(sample_statements))