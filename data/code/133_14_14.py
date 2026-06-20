def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        key, value = statement.split(': ')
        results[key.strip()] = value.lower() == 'true'
    return results

if __name__ == '__main__':
    sample_statements = [
        "The sky is blue: True",
        "2 + 2 equals five: False",
        "Python is awesome: True"
    ]
    print(evaluate_tf_statements(sample_statements))