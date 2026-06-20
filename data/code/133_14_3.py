def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        key, value = statement.split(': ')
        results[key] = value.strip().lower() == 'true'
    return results

if __name__ == '__main__':
    sample_statements = [
        "The sky is blue: True",
        "2 + 2 equals 5: False",
        "Python is awesome: True"
    ]
    print(evaluate_tf_statements(sample_statements))