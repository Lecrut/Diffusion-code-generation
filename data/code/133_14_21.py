def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        if ' is ' in statement:
            key, value = statement.split(' is ')
            results[key.strip()] = value.strip() == 'True'
        elif ' is not ' in statement:
            key, value = statement.split(' is not ')
            results[key.strip()] = value.strip() != 'False'
    return results

if __name__ == '__main__':
    sample_statements = [
        "1 + 1 is 2",
        "3 * 3 is not 9",
        "True is True",
        "False is False"
    ]
    print(evaluate_tf_statements(sample_statements))