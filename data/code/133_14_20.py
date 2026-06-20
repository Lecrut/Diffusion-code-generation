def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        key, value = statement.split(':')
        results[key.strip()] = value.strip().lower() == 'true'
    return results

if __name__ == '__main__':
    sample_values = [
        "The sky is blue: True",
        "2 + 2 = 5: False",
        "Python is awesome: True"
    ]
    print(evaluate_tf_statements(sample_values))