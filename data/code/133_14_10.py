def evaluate_tf_statements(statements):
    results = {}
    for statement in statements:
        parts = statement.split(': ')
        if len(parts) != 2:
            raise ValueError("Invalid statement format")
        key, value = parts[0], parts[1].strip().lower()
        if value not in ['true', 'false']:
            raise ValueError("Invalid boolean value")
        results[key] = value == 'true'
    return results

if __name__ == '__main__':
    sample_statements = [
        "The sky is blue: True",
        "2 + 2 equals 5: False",
        "Python is awesome: True"
    ]
    print(evaluate_tf_statements(sample_statements))